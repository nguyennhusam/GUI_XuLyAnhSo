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



# lớp ImageEditorClass thực hiện lớp cửa sổ chính GUI
class ImageEditorClass(QMainWindow):
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
        self.ui.viewHistogramButton.clicked.connect(lambda: self.view_histogram())
        
    # Hàm xử lý nút Open
    def open_image(self):
        #  Tạo hàm set_default_slider để xét các nút về vị trí ban đầu
        # self.set_default_slider()

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
            
    # Hàm enable_options bật tất cả các nút và thanh trượt trong cửa sổ.
    # Chỉ một nuts Open được mở khi bắt đầu
    def enable_options(self):
        self.ui.saveImageButton.setEnabled(True)
        
    # Tạo hàm set_default_slider để xét các nút về ban đầu
    # .......
    
    
    # Hàm khởi tạo ImageEditorClass và chạy ứng dụng
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = ImageEditorClass()
    myapp.showMaximized()
    sys.exit(app.exec_())
        

