import numpy as np
import cv2
import scipy


class ImageProcessorClass(object):
    def image_negative(self, image):
        image_row = image.shape[0]
        image_column = image.shape[1]

        image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
        output = np.uint8(255 * np.ones((image_row, image_column, 3)))
        output = output - image
        output = cv2.cvtColor(output, cv2.COLOR_BGR2HSV)

        return output

    def histogram_equalization(self, image):
        image_row = image.shape[0]
        image_column = image.shape[1]

        pmf = np.bincount(image.ravel(), minlength=256)
        pmf = pmf / (image_row * image_column)
        cdf = pmf.cumsum()
        pmf_lookup = np.uint8(np.floor(cdf * 255))
        output = image.copy()
        for r in range(256):
            output[image == r] = pmf_lookup[r]

        return output

    def gamma_correction(self, image, gamma):
        normalization_const = 255.0 / np.float_power(255, gamma)


        output = np.uint8(normalization_const * np.float_power(image, gamma))

        return output

    def log_transform(self, image):
        image_row = len(image)
        image_column = len(image[0])

        normalization_const = 255 / (np.log2(256))

        output = np.int8(normalization_const *
                         np.log2(image + np.ones((image_row, image_column))))

        return output

    def blur(self, image, window_size):
        window = np.ones((window_size, window_size), dtype=np.uint8)
        output = self.convolution(image, window)
        
        return output


    def sharp(self, image, sharp_const):
        window = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
        output = image - sharp_const * self.correlation(image, window)

        output[output < 0] = 0

        output[output > 255] = 255

        return output

    def edge_detection(self, image):
        window = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
        output = self.correlation(image, window)

        output[output < 0] = 0
        output[output > 255] = 255

        return output

    def convolution(self, image, window):
        window = np.flipud(np.fliplr(window))
        output = self.correlation(image, window)
        output = np.uint8(output / window.sum())

        return output


    def correlation(self, image, window):
        output = np.zeros_like(image)
        image_row = image.shape[0]
        image_column = image.shape[1]

        window_size = window.shape[0]
        zero_padding = window_size - 1
        offset = int(zero_padding / 2)

        image_zero_padded = \
            np.zeros((image_row + zero_padding, image_column + zero_padding))
        image_zero_padded[offset:(-1 * offset), offset:(-1 * offset)] = image

        for r in range(window_size):
            for c in range(window_size):
                output = output + window[r][c] * \
                         image_zero_padded[r:r + image_row, c:c + image_column]

        return output
    # def correlation(self, image, window):
    #     from scipy.signal import correlate2d
    #     output = correlate2d(image, window, mode='same')
    #     return output


