from PyQt5.QtWidgets import QFileDialog
import cv2

class FileDialogHandler:
    def __init__(self):
        # 定義全域變數 path
        self.path_1 = None

    def openFileDialog(self):
        print("openFileDialog 方法被觸發！")  # 檢查方法是否被觸發
        
        # # 彈出檔案選擇器，過濾文件類型
        # options = QFileDialog.Options()
        # options |= QFileDialog.ReadOnly  # 設定為只讀模式以確保功能正常

        # file_path, _ = QFileDialog.getOpenFileName(None, "選擇圖片檔案", "", "圖片文件 (*.jpg *.png *.bmp);;所有文件 (*)", options=options)
        
        # # 如果有選擇檔案，則載入並顯示檔案路徑
        # if file_path:
        #     print(f"已選擇檔案：{file_path}")
        #     # 儲存到全域變數 path
        #     self.path_1 = file_path
        #     # 使用 OpenCV 讀取圖片
        #     self.loaded_image = cv2.imread(file_path)
        # else:
        #     print("未選擇檔案")
