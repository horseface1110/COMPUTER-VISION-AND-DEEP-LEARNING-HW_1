import cv2, globals
import numpy as np
import matplotlib.pyplot as plt

def Gradient_Angle():
    if not globals.loaded_image_path_1 :
        print("請先輸入圖片_1")
        return
    image = cv2.imread(globals.loaded_image_path_1, cv2.IMREAD_GRAYSCALE) 

    
    # 計算 Sobel X 和 Y
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # 計算梯度角度 (以度數表示)
    gradient_angle = np.arctan2(sobely, sobelx) * (180 / np.pi)
    gradient_angle = np.mod(gradient_angle + 360, 360)  # 確保範圍在 [0, 360)

    # 產生兩個遮罩
    mask_170_190 = np.zeros_like(gradient_angle, dtype=np.uint8)
    mask_260_280 = np.zeros_like(gradient_angle, dtype=np.uint8)

    # 設定遮罩的條件
    mask_170_190[(gradient_angle >= 170) & (gradient_angle <= 190)] = 255
    mask_260_280[(gradient_angle >= 260) & (gradient_angle <= 280)] = 255

    # 計算梯度大小並增強對比度
    gradient_magnitude = np.sqrt(sobelx**2 + sobely**2)
    enhanced_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    enhanced_magnitude = cv2.convertScaleAbs(enhanced_magnitude, alpha=2.0, beta=0)  # 增加對比度

    # 位元操作 (AND) 來產生輸出
    result_170_190 = cv2.bitwise_and(enhanced_magnitude, enhanced_magnitude, mask=mask_170_190)
    result_260_280 = cv2.bitwise_and(enhanced_magnitude, enhanced_magnitude, mask=mask_260_280)

    # 顯示結果
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.title('Enhanced Gradient Magnitude')
    plt.imshow(enhanced_magnitude, cmap='gray')
    plt.subplot(1, 3, 2)
    plt.title('Angle 170° - 190°')
    plt.imshow(result_170_190, cmap='gray')
    plt.subplot(1, 3, 3)
    plt.title('Angle 260° - 280°')
    plt.imshow(result_260_280, cmap='gray')
    plt.show()