import cv2, globals
import numpy as np

def Gaussian_blur():
    if not globals.loaded_image_path_1 :
        print("請先輸入圖片_1")
        return
    image = cv2.imread(globals.loaded_image_path_1) 
    def apply_gaussian_blur(m):
        # 計算核大小 (2m + 1) × (2m + 1)
        kernel_size = (2 * m + 1, 2 * m + 1)
        # 應用高斯模糊
        blurred_image = cv2.GaussianBlur(image, kernel_size, sigmaX=0, sigmaY=0)
        # 顯示模糊後的圖片
        cv2.imshow('Gaussian Blur', blurred_image)

    # 創建視窗和滑桿
    cv2.namedWindow('Gaussian Blur')
    cv2.createTrackbar('Radius', 'Gaussian Blur', 1, 5, apply_gaussian_blur)
    
    # 初始應用高斯模糊（m=1）
    apply_gaussian_blur(1)