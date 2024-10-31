import cv2, globals
import numpy as np

def apply_transform(rotation, scaling, tx, ty):
    if not globals.loaded_image_path_1 :
        print("請先輸入圖片_1")
        return
    img = cv2.imread(globals.loaded_image_path_1) 
    
    # 設定圖片的中心點 C
    center_x, center_y = 240, 200  # 假設中心點在 (240, 200)

    # 1. 計算縮放矩陣
    M_scale = np.array([
        [scaling, 0, 0],
        [0, scaling, 0],
        [0, 0, 1]
    ])

    # 2. 計算旋轉矩陣 (逆時針)
    M_rotate = cv2.getRotationMatrix2D((center_x, center_y), rotation, 1)
    M_rotate = np.vstack([M_rotate, [0, 0, 1]])

    # 3. 計算平移矩陣
    M_translate = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

    # 4. 合併變換矩陣
    M = M_translate @ M_scale @ M_rotate

    # 取得圖片的寬和高
    (h, w) = img.shape[:2]

    # 進行仿射變換
    result = cv2.warpAffine(img, M[:2], (1920, 1080))

    # 顯示結果
    cv2.imshow("Transformed Image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
