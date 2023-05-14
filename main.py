import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *

import cv2
import numpy as np
import matplotlib.pyplot as plt

from gui import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFileDialog

import imageProcessingFns as ip

# lớp ImageEditorClass thực hiện lớp cửa sổ chính GUI
class ImageEditorClass(QMainWindow):
    originalImage = [0]

    currentImage = [0]

    previousImage = [0]

    imageLogTransform = [0]

    imageBlur = [0]

    imageSharpen = [0]

    imageWidth = 0
    imageHeight = 0

    # initializes an object of ImageProcessorClass from imageProcessingFns.py
    imageLib = ip.ImageProcessorClass()

    # stores code of current operation
    currentOperationCode = -1
    
    def __init__(self, parent=None):
        super(ImageEditorClass, self).__init__()
        QWidget.__init__(self, parent)
        self.ui = ImageEditorGuiClass()
        self.ui.setupUi(self)

        # Chỉ định các chức năng được gọi trên tất cả các sự kiện được nhấp vào 
        # và các sự kiện đã thay đổi giá trị thanh trượt

        self.ui.openImageButton.clicked.connect(lambda: self.open_image())
        self.ui.saveImageButton.clicked.connect(lambda: self.save_image())
        self.ui.histogramEqualizationButton.clicked.connect\
            (lambda: self.histogram_equalization())
        self.ui.logTransformButton.clicked.connect(lambda: self.log_transform())
        self.ui.logTransformSlider.valueChanged.connect(lambda: self.log_transform())
        self.ui.gammaCorrectionButton.clicked.connect(lambda: self.gamma_correction())
        self.ui.negativeButton.clicked.connect(lambda: self.image_negative())

        self.ui.blurExtendInputSlider.valueChanged.connect(lambda: self.blur())
        self.ui.sharpenExtendInputSlider.valueChanged.connect(lambda: self.sharpen())

        self.ui.undoButton.clicked.connect(lambda: self.undo())
        self.ui.undoAllButton.clicked.connect(lambda: self.undoAll())
        
        self.ui.viewHistogramButton.clicked.connect(lambda: self.view_histogram())
        self.ui.detectEdgeButton.clicked.connect(lambda: self.edge_detection())
        
        self.newDialog = InputDialogGuiClass(self)
        
    # Hàm xử lý nút Open
    def open_image(self):
        #  Tạo hàm set_default_slider để xét các nút về vị trí ban đầu
        self.set_default_slider()

        # Mở hộp thoại Mở hình ảnh mới và chụp đường dẫn của tệp đã chọn
        open_image_window = QFileDialog()
        image_path, _ = open_image_window.getOpenFileName(None, 'Open Image','','Image Files (*.png *.jpg *.bmp)')

        # Kiểm tra xem đường dẫn hình ảnh không rỗng hay trống
        if image_path:
            self.currentImage = [0]
            self.currentOperationCode = -1

            # Đọc hình ảnh tại đường dẫn đã chọn đến đối tượng ndarray gọn gàng dưới dạng hình ảnh màu
            self.currentImage = cv2.imread(image_path, 1)
            # Chuyển đổi hình ảnh đã đọc sang định dạng HSV từ định dạng BGR mặc định
            self.currentImage = cv2.cvtColor(self.currentImage, cv2.COLOR_BGR2HSV)

            # Đặt các biến lớp cụ thể của hình ảnh dựa trên hình ảnh hiện tại
            self.imageWidth = self.currentImage.shape[1]
            self.imageHeight = self.currentImage.shape[0]

            self.originalImage = self.currentImage.copy()
            self.previousImage = self.currentImage.copy()

            # displayImage chuyển đổi hình ảnh hiện tại từ định dạng darrry sang pixmap và gán nó cho nhãn hiển thị hình ảnh
            self.displayImage()
            # enable_options bật tất cả các nút trong cửa sổ.
            # Các thao tác chỉnh sửa sẽ được hiển thị khi Open ảnh thành công
            self.enable_options()
            
    # Hàm xử lý nút Save
    def save_image(self):
        # Lưu ảnh dưới dạng file .jpg
        dialog = QFileDialog()
        dialog.setDefaultSuffix('jpg')
        dialog.setAcceptMode(QFileDialog.AcceptSave)

        # Mở hộp thoại để lưu ảnh
        if dialog.exec_() == QDialog.Accepted:
            # Chọn đường dẫn đầu tiên trong danh sách tệp đã chọn làm vị trí lưu ảnh
            save_image_filename = dialog.selectedFiles()[0]
            # Đặt tên file để  lưu
            cv2.imwrite(save_image_filename,
                        cv2.cvtColor(self.currentImage, cv2.COLOR_HSV2BGR))
            
            
            
    # Hàm hiển thị hình ảnh khi thêm ảnh thành công từ folder
    def displayImage(self):
        display_size = self.ui.imageDisplayLabel.size()
        image = np.array(self.currentImage.copy())
        zero = np.array([0])
        
        if not np.array_equal(image, zero):
            image = cv2.cvtColor(image, cv2.COLOR_HSV2RGB)
            qImage = QImage(image, self.imageWidth, self.imageHeight,
                            self.imageWidth * 3, QImage.Format_RGB888)
            
            pixmap = QPixmap()
            QPixmap.convertFromImage(pixmap, qImage)
            pixmap = pixmap.scaled(display_size, Qt.KeepAspectRatio,
                                   Qt.SmoothTransformation)
            self.ui.imageDisplayLabel.setPixmap(pixmap)
            
    #
    def histogram_equalization(self):
        self.updatePreviousImage()
        self.currentOperationCode = 0
        self.set_default_slider()

        self.currentImage[:, :, 2] = self.imageLib.histogram_equalization\
            (self.currentImage[:, :, 2])
        # for i in range(3):
        #     self.currentImage[:, :, i] = self.imageLib.histogram_equalization(self.currentImage[:, :, i])
            
        self.displayImage()

    def gamma_correction(self):
        self.updatePreviousImage()

        self.currentOperationCode = 1

        self.set_default_slider()

        if self.newDialog.exec() == 0:
            gamma_value = self.newDialog.gamma
            self.newDialog.gammaInput.setText('1.00')
            self.newDialog.gamma = 1.0
            if gamma_value > 0:
                self.currentImage[:, :, 2] = self.imageLib.gamma_correction\
                    (self.currentImage[:, :, 2], gamma_value)

        self.displayImage()

    def log_transform(self):
        self.updatePreviousImage()
        
        self.ui.logTransformSlider.valueChanged.connect(lambda: self.log_transform())
        logTranform_value = int(np.floor(self.ui.logTransformSlider.value()))


        self.currentOperationCode = 2


        # self.currentImage[:, :, 2] = \
        #     self.imageLib.log_transform(self.currentImage[:, :, 2])
        for i in range(3):
            self.currentImage[:, :, i] = self.imageLib.log_transform(self.currentImage[:, :, i])
        self.ui.logTransformValueLabel.setText(str(logTranform_value))
        self.displayImage()

    def image_negative(self):
        self.updatePreviousImage()
        self.currentOperationCode = 3
        
        self.set_default_slider()

        self.currentImage = self.imageLib.image_negative(self.currentImage)

        self.displayImage()

    def blur(self):
        self.updatePreviousImage()

        self.ui.sharpenExtendInputSlider.valueChanged.disconnect()
        self.ui.sharpenExtendInputSlider.setValue(0)
        self.ui.sharpenExtendInputSlider.valueChanged.connect(lambda:
                                                              self.sharpen())
        self.ui.sharpenValueLabel.setText('0')

        blur_value = int(np.floor(self.ui.blurExtendInputSlider.value()))
        blur_window_size = (blur_value * 2) + 1

        if self.currentOperationCode == 4:
            self.currentImage = self.imageBlur.copy()
        else:
            self.imageBlur = self.currentImage.copy()

        if blur_value > 0:
            # enable undo button
            self.ui.undoButton.setEnabled(True)
            # self.currentImage[:, :, 2] = \
            #     self.imageLib.blur(self.currentImage[:, :, 2], blur_window_size)
            for i in range(3):
                self.currentImage[:, :, i] = self.imageLib.blur(self.currentImage[:, :, i],blur_window_size)

        self.currentOperationCode = 4

        self.ui.blurValueLabel.setText(str(blur_value))
        self.displayImage()

    def sharpen(self):
        self.updatePreviousImage()

        self.ui.blurExtendInputSlider.valueChanged.disconnect()
        self.ui.blurExtendInputSlider.setValue(0)
        self.ui.blurExtendInputSlider.valueChanged.\
            connect(lambda: self.blur())
        self.ui.blurValueLabel.setText('0')

        sharpen_value = self.ui.sharpenExtendInputSlider.value()
        sharpen_const = sharpen_value / 10.0

        if self.currentOperationCode == 5:
            self.currentImage = self.imageSharpen.copy()
        else:
            self.imageSharpen = self.currentImage.copy()

        if sharpen_const > 0:
            # enable undo button
            self.ui.undoButton.setEnabled(True)
            # self.currentImage[:, :, 2] = \
            #     np.uint8(self.imageLib.sharp(self.currentImage[:, :, 2], sharpen_const))
            for i in range(3):
                self.currentImage[:, :, i] = self.imageLib.sharp(self.currentImage[:, :, i],sharpen_const)

        self.currentOperationCode = 5

        self.ui.sharpenValueLabel.setText(str(sharpen_value))

        self.displayImage()

    def undo(self):
        self.ui.undoButton.setEnabled(False)
        self.currentImage = self.previousImage.copy()

        self.displayImage()

    def undoAll(self):
        self.set_default_slider()
        self.currentImage = self.originalImage.copy()

        self.displayImage()
        self.ui.undoButton.setEnabled(False)

    def view_histogram(self):
        # histogramRed = np.bincount(self.currentImage[:, :, 0].ravel(), minlength=256)
        # histogramBlue = np.bincount(self.currentImage[:, :, 1].ravel(), minlength=256)
        # histogramGreen = np.bincount(self.currentImage[:, :, 2].ravel(), minlength=256)
        
        # plt.figure(num='Image Histogram')
        
        # plt.fill_between(np.arange(256), histogramRed, color='r', alpha=0.5)
        # plt.fill_between(np.arange(256), histogramGreen, color='g', alpha=0.5)
        # plt.fill_between(np.arange(256), histogramBlue, color='b', alpha=0.5)
        
        # plt.xlabel('Intensity levels')
        # plt.ylabel('No. of pixels')
        # plt.show()
        hist_r = np.zeros(256)
        hist_g = np.zeros(256)
        hist_b = np.zeros(256)
        for i in range(self.currentImage.shape[0]):
            for j in range(self.currentImage.shape[1]):
                r = self.currentImage[i,j,0]
                g = self.currentImage[i,j,1]
                b = self.currentImage[i,j,2]
                hist_r[r] += 1
                hist_g[g] += 1
                hist_b[b] += 1
        hist_all = hist_r + hist_g + hist_b

        # Hiển thị biểu đồ histogram
        fig, ax = plt.subplots(2, 2, figsize=(10, 8))
        ax[0, 0].bar(np.arange(256), hist_r, color='r', alpha=0.5)
        ax[0, 1].bar(np.arange(256), hist_g, color='g', alpha=0.5)
        ax[1, 0].bar(np.arange(256), hist_b, color='b', alpha=0.5)
        ax[1, 1].bar(np.arange(256), hist_all, color='k', alpha=0.5)
        ax[0, 0].set_ylabel('Số lượng pixel')
        ax[0, 1].set_ylabel('Số lượng pixel')
        ax[1, 0].set_ylabel('Số lượng pixel')
        ax[1, 1].set_ylabel('Số lượng pixel')
        ax[1, 1].set_xlabel('Giá trị màu (0-255)')
        ax[0, 0].set_title('Biểu đồ histogram R')
        ax[0, 1].set_title('Biểu đồ histogram G')
        ax[1, 0].set_title('Biểu đồ histogram B')
        ax[1, 1].set_title('Biểu đồ histogram tổng hợp')
        plt.tight_layout()
        plt.show()
        





    def edge_detection(self):
        self.updatePreviousImage()

        self.currentOperationCode = 6
        self.set_default_slider()
        # self.currentImage[:, :, 2] \
        #     = self.imageLib.edge_detection(self.currentImage[:, :, 2])
        
        for i in range(3):
            self.currentImage[:, :, i] = self.imageLib.edge_detection(self.currentImage[:, :, i])

        self.displayImage()
            
    # Hàm enable_options bật tất cả các nút và thanh trượt trong cửa sổ.
    # Chỉ một nuts Open được mở khi bắt đầu
    def enable_options(self):
        self.ui.saveImageButton.setEnabled(True)
        
        self.ui.histogramEqualizationButton.setEnabled(True)
        self.ui.gammaCorrectionButton.setEnabled(True)
        self.ui.logTransformButton.setEnabled(True)
        self.ui.logTransformSlider.setEnabled(True)
        self.ui.negativeButton.setEnabled(True)

        self.ui.blurExtendInputSlider.setEnabled(True)
        self.ui.sharpenExtendInputSlider.setEnabled(True)

        self.ui.undoAllButton.setEnabled(True)
        self.ui.undoButton.setEnabled(False)

        self.ui.viewHistogramButton.setEnabled(True)
        self.ui.detectEdgeButton.setEnabled(True)
        
    # Tạo hàm set_default_slider để xét các nút về ban đầu
    # .......
    def set_default_slider(self):
        self.ui.logTransformSlider.valueChanged.disconnect()
        self.ui.sharpenExtendInputSlider.valueChanged.disconnect()
        self.ui.blurExtendInputSlider.valueChanged.disconnect()

        self.ui.logTransformSlider.setValue(0)
        self.ui.logTransformValueLabel.setText('0')
        self.ui.blurExtendInputSlider.setValue(0)
        self.ui.blurValueLabel.setText('0')
        self.ui.sharpenExtendInputSlider.setValue(0)
        self.ui.sharpenValueLabel.setText('0')

        self.ui.logTransformSlider.valueChanged.connect(lambda: self.log_transform())
        self.ui.blurExtendInputSlider.valueChanged.connect(lambda: self.blur())
        self.ui.sharpenExtendInputSlider.valueChanged.connect(lambda: self.sharpen())

        self.imageLogTransform = [0]
        self.imageBlur = [0]
        self.imageSharpen = [0]

        if (self.currentOperationCode >= 0) and \
                not self.ui.undoButton.isEnabled():
            self.ui.undoButton.setEnabled(True)


    def updatePreviousImage(self):
        self.previousImage = self.currentImage.copy()
    
    
    # Hàm khởi tạo ImageEditorClass và chạy ứng dụng
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = ImageEditorClass()
    myapp.showMaximized()
    sys.exit(app.exec_())
        

