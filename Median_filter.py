import cv2, globals
import numpy as np

def Median_filter():
    if not globals.loaded_image_path_1 :
        print("請先輸入圖片_1")
        return
    image = cv2.imread(globals.loaded_image_path_1) 
    def update_median_blur(val):
        # 計算 kernel size (2m + 1)
        m = max(1, val)  # 確保至少為1
        kernel_size = 2 * m + 1

        # 應用中值濾波器
        blurred_image = cv2.medianBlur(image, kernel_size)

        # 顯示處理後的圖片
        cv2.imshow("Median Filtered Image", blurred_image)

    # 創建顯示窗口
    cv2.namedWindow("Median Filtered Image")

    # 創建滑桿，範圍是 1 到 5
    cv2.createTrackbar("Radius (m)", "Median Filtered Image", 1, 5, update_median_blur)

    # 初始化顯示
    update_median_blur(1)

    # 等待直到按下任意鍵
    cv2.waitKey(0)
    cv2.destroyAllWindows()