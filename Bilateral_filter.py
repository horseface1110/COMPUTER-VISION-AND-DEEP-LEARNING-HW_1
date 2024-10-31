import cv2, globals
import numpy as np

def Bilateral_filter():
    if not globals.loaded_image_path_1 :
        print("請先輸入圖片_1")
        return
    image = cv2.imread(globals.loaded_image_path_1) 
    # 定義雙邊濾波函數，使用滑桿更新核大小
    def apply_bilateral_filter(m):
        # 計算核的直徑 (2m + 1)
        diameter = 2 * m + 1
        # 設定 sigmaColor 和 sigmaSpace
        sigmaColor = 90
        sigmaSpace = 90
        # 應用雙邊濾波
        bilateral_image = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
        # 顯示模糊後的圖片
        cv2.imshow('Bilateral Filter', bilateral_image)

    # 創建視窗
    cv2.namedWindow('Bilateral Filter')

    # 創建滑桿，範圍是 1 到 5（對應 m = 1 到 5）
    cv2.createTrackbar('Radius', 'Bilateral Filter', 1, 5, apply_bilateral_filter)

    # 初始應用雙邊濾波（m=1）
    apply_bilateral_filter(1)

    # 等待按鍵
    cv2.waitKey(0)
    cv2.destroyAllWindows()