from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtGui import QIcon,QPixmap

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)
    
    
# Lớp xác định tất cả các phần tử GUI cho cửa sổ ứng dụng Chính

class ImageEditorGuiClass(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(886, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                       QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Dyuthi"))
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        
        
        # Xác định bố cục cho window
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.verticalLayout.addWidget(self.line_7)
        
        # Xác định khu vực hiển thị hình ảnh
        self.imageDisplayLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageDisplayLabel.setAlignment(QtCore.Qt.AlignHCenter
                                            |QtCore.Qt.AlignVCenter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                       QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageDisplayLabel.sizePolicy().
                                     hasHeightForWidth())
        self.imageDisplayLabel.setSizePolicy(sizePolicy)
        self.imageDisplayLabel.setAutoFillBackground(False)
        self.imageDisplayLabel.setStyleSheet(_fromUtf8("background-color: "
                                                       "#000000"))
        backgroundPixmap = QPixmap('background.png')
        self.imageDisplayLabel.setPixmap(backgroundPixmap)
        self.imageDisplayLabel.setText(_fromUtf8(""))
        self.imageDisplayLabel.setObjectName(_fromUtf8("imageDisplayLabel"))
        self.verticalLayout.addWidget(self.imageDisplayLabel)

        self.gridLayout_2.addLayout(self.verticalLayout, 1, 3, 2, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        
        
        # Xác định nút Open để thêm ảnh
        self.openImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.openImageButton.setObjectName(_fromUtf8("openImageButton"))
        self.horizontalLayout.addWidget(self.openImageButton)
        self.openImageButton.setStyleSheet("background-color:#1D267D; color: white;")
        self.openImageButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # Xác định nút Save ảnh
        self.saveImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveImageButton.setObjectName(_fromUtf8("saveImageButton"))
        self.saveImageButton.setEnabled(False)
        self.horizontalLayout.addWidget(self.saveImageButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout_3.addWidget(self.line_6)
        self.saveImageButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        # Xác định Histogram Equalization button
        self.histogramEqualizationButton = QtWidgets.QPushButton(self.centralwidget)
        self.histogramEqualizationButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.
                                       QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogramEqualizationButton.
                                     sizePolicy().hasHeightForWidth())
        self.histogramEqualizationButton.setSizePolicy(sizePolicy)
        self.histogramEqualizationButton.setObjectName(
            _fromUtf8("histogramEqualizationButton"))
        self.verticalLayout_3.addWidget(self.histogramEqualizationButton)
        
        # Xác định View Histogram button
        self.viewHistogramButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewHistogramButton.setObjectName(_fromUtf8("viewHistogramButton"))
        self.verticalLayout_3.addWidget(self.viewHistogramButton)

        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.verticalLayout_3.addWidget(self.line_10)
        
        # Xác định Gamma Correction button
        self.gammaCorrectionButton = QtWidgets.QPushButton(self.centralwidget)
        self.gammaCorrectionButton.setObjectName(_fromUtf8("gammaCorrectionButton"))
        self.gammaCorrectionButton.setEnabled(False)
        self.verticalLayout_3.addWidget(self.gammaCorrectionButton)
        
        # Xác định Log Transform button
        self.logTransformButton = QtWidgets.QPushButton(self.centralwidget)
        self.logTransformButton.setObjectName(_fromUtf8("logTransformButton"))
        self.logTransformButton.setEnabled(False)
        self.verticalLayout_3.addWidget(self.logTransformButton)
        
        # Xác định Image Negative button
        self.negativeButton = QtWidgets.QPushButton(self.centralwidget)
        self.negativeButton.setObjectName(_fromUtf8("negativeButton"))
        self.negativeButton.setEnabled(False)
        self.verticalLayout_3.addWidget(self.negativeButton)

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        
        # Xác định Blur Slider Name label
        self.blurLabel = QtWidgets.QLabel(self.centralwidget)
        self.blurLabel.setObjectName(_fromUtf8("blurLabel"))
        self.horizontalLayout_9.addWidget(self.blurLabel)

        self.blurValueLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                       QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blurValueLabel.sizePolicy()
                                     .hasHeightForWidth())
        
        # Xác định Blur Slider Value label
        self.blurValueLabel.setSizePolicy(sizePolicy)
        self.blurValueLabel.setAlignment(QtCore.Qt.AlignRight|QtCore
                                         .Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.blurValueLabel.setObjectName(_fromUtf8("blurValueLabel"))
        self.horizontalLayout_9.addWidget(self.blurValueLabel)

        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        
        # Xác định blur slider
        self.blurExtendInputSlider = QtWidgets.QSlider(self.centralwidget)
        self.blurExtendInputSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blurExtendInputSlider.setObjectName(_fromUtf8("blurExtendInputSlider"))
        self.blurExtendInputSlider.setRange(0,10)
        self.blurExtendInputSlider.setEnabled(False)
        self.verticalLayout_3.addWidget(self.blurExtendInputSlider)

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_3.addWidget(self.line_3)

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        
        # Xác định Sharpen Slider Name label
        self.sharpenLabel = QtWidgets.QLabel(self.centralwidget)
        self.sharpenLabel.setObjectName(_fromUtf8("sharpenLabel"))
        self.horizontalLayout_10.addWidget(self.sharpenLabel)

        self.sharpenValueLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                       QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sharpenValueLabel.sizePolicy()
                                     .hasHeightForWidth())

        # Xác định Sharpen Slider Value label
        self.sharpenValueLabel.setSizePolicy(sizePolicy)
        self.sharpenValueLabel.setAlignment(QtCore.Qt.AlignRight|QtCore
                                            .Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sharpenValueLabel.setObjectName(_fromUtf8("sharpenValueLabel"))
        self.horizontalLayout_10.addWidget(self.sharpenValueLabel)

        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        # Xác định Sharpen Slider
        self.sharpenExtendInputSlider = QtWidgets.QSlider(self.centralwidget)
        self.sharpenExtendInputSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sharpenExtendInputSlider.setObjectName(
            _fromUtf8("sharpenExtendInputSlider"))
        self.sharpenExtendInputSlider.setRange(0, 10)
        self.sharpenExtendInputSlider.setEnabled(False)
        self.verticalLayout_3.addWidget(self.sharpenExtendInputSlider)

        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_3.addWidget(self.line_4)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        
        # Xác định Undo button
        self.undoButton = QtWidgets.QPushButton(self.centralwidget)
        self.undoButton.setObjectName(_fromUtf8("undoButton"))
        self.undoButton.setEnabled(False)
        self.horizontalLayout_4.addWidget(self.undoButton)

        # Xác định Undo All button
        self.undoAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.undoAllButton.setObjectName(_fromUtf8("undoAllButton"))
        self.undoAllButton.setEnabled(False)
        self.horizontalLayout_4.addWidget(self.undoAllButton)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        
        # Xác dịnh Edge Detection button
        self.detectEdgeButton = QtWidgets.QPushButton(self.centralwidget)
        self.detectEdgeButton.setObjectName(_fromUtf8("detectEdgeButton"))
        self.verticalLayout_3.addWidget(self.detectEdgeButton)

        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.verticalLayout_3.addWidget(self.line_9)

        self.detectEdgeButton.setEnabled(False)
        self.viewHistogramButton.setEnabled(False)
        
        
        
         # Xác định pannel thành viên
        self.textboxTV1 = QtWidgets.QLabel(self.centralwidget)
        self.textboxTV1.setObjectName(_fromUtf8("textboxTV1"))
        self.verticalLayout_3.addWidget(self.textboxTV1)
        self.textboxTV1.setEnabled(False)

        self.textboxTV2 = QtWidgets.QLabel(self.centralwidget)
        self.textboxTV2.setObjectName(_fromUtf8("textboxTV2"))
        self.verticalLayout_3.addWidget(self.textboxTV2)
        self.textboxTV2.setEnabled(False)

        self.textboxTV3 = QtWidgets.QLabel(self.centralwidget)
        self.textboxTV3.setObjectName(_fromUtf8("textboxTV3"))
        self.verticalLayout_3.addWidget(self.textboxTV3)
        self.textboxTV3.setEnabled(False)


       

        
        # ProgressLabel is not used
        self.progressLabel = QtWidgets.QLabel(self.centralwidget)
        self.progressLabel.setText(_fromUtf8(""))
        self.progressLabel.setObjectName(_fromUtf8("progressLabel"))
        self.verticalLayout_3.addWidget(self.progressLabel)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                       QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 2, 0, 1, 2)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))

        self.gridLayout_2.addWidget(self.line_5, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 886, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        
      
        # Đặt tên cho các thành phần của GUI
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate
                                  ("MainWindow", "GUI Xử lý ảnh - Nhóm 4", None))
        self.openImageButton.setText(_translate
                                     ("MainWindow", "Open", None))
        self.saveImageButton.setText(_translate
                                     ("MainWindow", "Save", None))
        icon = QIcon("logo2.png")
        pixmap = icon.pixmap(64, 64)
        MainWindow.setWindowIcon(QIcon(pixmap))
        
        self.histogramEqualizationButton.setText(_translate
                                                 ("MainWindow", "Histogram Equalization", None))
        self.gammaCorrectionButton.setText(_translate
                                           ("MainWindow", "Gamma Correction", None))
        self.logTransformButton.setText(_translate
                                        ("MainWindow", "Log Transform", None))
        self.negativeButton.setText(_translate
                                    ("MainWindow", "Image Negative", None))
        self.blurLabel.\
            setText(_translate("MainWindow",
                               "<html><head/><body><p>Blur Image</p></body></html>", None))
        self.blurValueLabel.setText(_translate("MainWindow", "0", None))
        self.sharpenLabel.setText(_translate
                                  ("MainWindow", "Sharpen Image", None))
        self.sharpenValueLabel.setText(_translate
                                       ("MainWindow", "0", None))
        self.undoButton.setText(_translate
                                ("MainWindow", "Undo", None))
        self.undoAllButton.setText(_translate
                                   ("MainWindow", "Undo All", None))
        self.detectEdgeButton.setText(_translate
                                      ("MainWindow", "Edge Detection", None))
        self.viewHistogramButton.setText(_translate
                                         ("MainWindow", "View Histogram", None))
        self.textboxTV1.setText(_translate
                                         ("MainWindow", "Trần Đức Long - 20110058", None))
        self.textboxTV2.setText(_translate
                                         ("MainWindow", "Nguyễn Như Sâm - 20110557", None))
        self.textboxTV3.setText(_translate
                                         ("MainWindow", "Đào Xuân Trí - 20110581", None))
    
    
    
        
class InputDialogGuiClass(QDialog):
    gamma = 1.0

    def __init__(self, parent):
        super(InputDialogGuiClass, self).__init__(parent)
        self.setupUi(self)

        self.cancelButton.clicked.connect(lambda: self.close_window())
        self.okButton.clicked.connect(lambda: self.accept_value())

    def setupUi(self, InputDialogGuiClass):
        InputDialogGuiClass.setObjectName(_fromUtf8("InputDialogGuiClass"))
        InputDialogGuiClass.setWindowModality(QtCore.Qt.WindowModal)
        InputDialogGuiClass.setFixedWidth(360)
        InputDialogGuiClass.setFixedHeight(140)
        self.verticalLayout = QtWidgets.QVBoxLayout(InputDialogGuiClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtWidgets.QLabel(InputDialogGuiClass)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.gammaInput = QtWidgets.QLineEdit(InputDialogGuiClass)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gammaInput.sizePolicy().hasHeightForWidth())
        self.gammaInput.setSizePolicy(sizePolicy)
        self.gammaInput.setObjectName(_fromUtf8("lineEdit"))
        self.gammaInput.setText('1.00')
        self.gammaInput.setValidator(QtGui.QDoubleValidator(0, 10.0, 2, self.gammaInput))
        self.horizontalLayout_2.addWidget(self.gammaInput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(InputDialogGuiClass)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                       QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.cancelButton = QtWidgets.QPushButton(InputDialogGuiClass)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_3.addWidget(self.cancelButton)
        self.okButton = QtWidgets.QPushButton(InputDialogGuiClass)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout_3.addWidget(self.okButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(InputDialogGuiClass)
        QtCore.QMetaObject.connectSlotsByName(InputDialogGuiClass)

    def close_window(self):
        self.close()

    def accept_value(self):
        if self.gammaInput.text() and float(self.gammaInput.text()) <= 10.0:
            self.gamma = float(self.gammaInput.text())
            self.close()
            return True
        else:
            self.label_2.setStyleSheet("color: rgb(255, 0, 0);")


    def retranslateUi(self, InputDialogGuiClass):
        InputDialogGuiClass.setWindowTitle(_translate("InputDialogGuiClass",
                                                      "Enter Gamma Value", None))
        self.label.setText(_translate("InputDialogGuiClass", "Gamma", None))
        self.label_2.setText(_translate("InputDialog",
                                        "NB: Enter a value between 0 and 10", None))
        self.cancelButton.setText(_translate("InputDialog", "Cancel", None))
        self.okButton.setText(_translate("InputDialog", "OK", None))
        
        



