import cv2, globals
import numpy as np

def Color_Extraction():
    if not globals.loaded_image_path_1 :
        print("請先輸入圖片_1")
        return
    image = cv2.imread(globals.loaded_image_path_1) 

    # 將 BGR 轉換為 HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 建立黃綠色遮罩
    # 定義黃綠色的 HSV 範圍 (需要根據實際圖片調整上下限)
    lower_bound = np.array([18, 0, 25])  # HSV 下限
    upper_bound = np.array([85, 255, 255])  # HSV 上限

    # 使用 inRange 函數創建黃綠色遮罩
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

    # 反轉遮罩
    mask_inverse = cv2.bitwise_not(mask)

    # 去除圖片中的黃綠色
    extracted_image = cv2.bitwise_and(image, image, mask=mask_inverse)

    # 顯示結果
    cv2.imshow('Original Image', image)
    cv2.imshow('Yellow-Green Mask', mask)
    cv2.imshow('Inversed Mask', mask_inverse)
    cv2.imshow('Image without Yellow-Green', extracted_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()