import cv2, globals
import numpy as np

def Sobel_X():
    if not globals.loaded_image_path_1 :
        print("請先輸入圖片_1")
        return
    image = cv2.imread(globals.loaded_image_path_1) 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用高斯模糊平滑化圖片
    blurred = cv2.GaussianBlur(gray, (5, 5), sigmaX=1, sigmaY=1)

    # 定義3x3的Sobel X核，用於檢測垂直邊緣
    sobel_x_kernel = np.array([[-1, 0, 1],
                            [-2, 0, 2],
                            [-1, 0, 1]])

    # 自定義的卷積操作
    def apply_custom_convolution(image, kernel):
        # 初始化輸出圖片
        output = np.zeros_like(image)
        
        # 取得核的尺寸
        kernel_size = kernel.shape[0]
        pad = kernel_size // 2
        
        # 在灰階圖片周圍添加填充（邊界）
        padded_image = np.pad(image, ((pad, pad), (pad, pad)), mode='constant', constant_values=0)
        
        # 卷積操作
        for i in range(pad, padded_image.shape[0] - pad):
            for j in range(pad, padded_image.shape[1] - pad):
                region = padded_image[i - pad:i + pad + 1, j - pad:j + pad + 1]
                output[i - pad, j - pad] = abs(np.sum(region * kernel))  # 取絕對值避免負數
        
        return output

    # 對模糊圖片應用自定義的Sobel X卷積
    globals.sobel_x_result = apply_custom_convolution(blurred, sobel_x_kernel)

    # 顯示結果
    cv2.imshow("Sobel X", globals.sobel_x_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()