import cv2
import globals
import numpy as np

def Color_Transformation():
    # 讀取彩色圖片
    if not globals.loaded_image_path_1 :
        print("請先輸入圖片_1")
        return
    image = cv2.imread(globals.loaded_image_path_1)  

    # 使用 cv2.cvtColor 將彩色圖片轉換為灰階圖片
    cv_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 分離 B、G、R 通道
    b, g, r = cv2.split(image)

    # 計算每個像素的 B、G、R 平均值，並轉換為 uint8
    avg_gray = ((b / 3) + (g / 3) + (r / 3)).astype(np.uint8)

    # 顯示灰階圖片
    cv2.imshow('Gray Image', cv_gray)
    
    # 顯示灰階圖片
    cv2.imshow('Average Gray Image', avg_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()