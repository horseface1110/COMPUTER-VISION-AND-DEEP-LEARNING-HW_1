import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from qt_test import Ui_MainWindow  # 載入生成的 UI 模組
from color_separation_handler import handle_color_separation  # 導入分離的處理函式   
from file_dialog_handler_1 import FileDialogHandler  # 導入新建的文件選擇處理類別
import cv2
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 定義變數來儲存圖片
        self.loaded_image = None

        # self.Color_Separation.clicked.connect(handle_color_separation)  ## Color_Separation 功能綁定
        self.Load_Image_1.clicked.connect(FileDialogHandler.openFileDialog)  # 綁定載入圖片按鈕到新的文件選擇方法
        print("按鈕初始化完成，等待點擊事件...")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())