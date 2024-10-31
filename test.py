import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from qt_test import Ui_MainWindow  # 載入生成的 UI 模組
from color_separation_handler import handle_color_separation  # 導入分離的處理函式   
from Color_Transformation import Color_Transformation
from Color_Extraction import Color_Extraction
from Gaussian_blur import Gaussian_blur
from Bilateral_filter import Bilateral_filter
from Median_filter import Median_filter
from Sobel_X import Sobel_X
from Sobel_Y import Sobel_Y
from Combination_and_Threshold import Combination_and_Threshold
from Gradient_Angle import Gradient_Angle
from transform_functions import apply_transform
import cv2, globals
from PyQt5.QtCore import Qt

# 定義全域變數來儲存圖片路徑
globals.loaded_image_path_1 = None

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        ## 第零部分
        self.Load_Image_1.clicked.connect(self.load_image)  # 綁定載入圖片按鈕到load_image方法
        
        ## 第一部分各項功能
        self.Color_Separation.clicked.connect(handle_color_separation)  ## Color_Separation 功能綁定
        self.Color_Transformation.clicked.connect(Color_Transformation) ## Color_Transformation 功能綁定
        self.Color_Extraction.clicked.connect(Color_Extraction) ## Color_Extraction 功能綁定
        
        ## 第二部分
        self.Gaussian_blur.clicked.connect(Gaussian_blur) ## Caussian_blur 功能綁定
        self.Bilateral_filter.clicked.connect(Bilateral_filter)
        self.Median_filter.clicked.connect(Median_filter)
        
        ## 第三部分
        self.Sobel_X.clicked.connect(Sobel_X)
        self.Sobel_Y.clicked.connect(Sobel_Y)
        self.Combination_and_Threshold.clicked.connect(Combination_and_Threshold)
        self.Gradient_Angle.clicked.connect(Gradient_Angle)
        
        ## 第四部份
        self.Transforms.clicked.connect(self.on_transform_button_clicked)
        print("按鈕初始化完成，等待點擊事件...")

    def load_image(self):
        # 打開文件對話框，選擇圖片
        file_name, _ = QFileDialog.getOpenFileName(self, "選擇圖片", "", "Image Files (*.png *.jpg *.bmp)")
        if file_name:
            globals.loaded_image_path_1 = file_name  # 儲存圖片路徑到變數
            print(f"圖片已載入：{globals.loaded_image_path_1}")  # 打印圖片路徑確認
            
    def on_transform_button_clicked(self):
        # 取得使用者輸入的參數
        rotation = float(self.Rotation.text()) if self.Rotation.text() else 0
        scaling = float(self.Scaling.text()) if self.Scaling.text() else 1
        tx = int(self.Tx.text()) if self.Tx.text() else 0
        ty = int(self.Ty.text()) if self.Ty.text() else 0

        # 執行圖片變換
        apply_transform(rotation, scaling, tx, ty)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())