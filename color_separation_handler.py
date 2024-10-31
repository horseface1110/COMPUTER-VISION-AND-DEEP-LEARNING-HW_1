# color_separation_handler.py
import globals
import cv2

def handle_color_separation():
    # 在這裡編寫 Color Separation 按鈕的功能
    print("Color Separation button clicked!")
    
    if not globals.loaded_image_path_1 :
        print("請先輸入圖片_1")
        return
    else:
        img = cv2.imread(globals.loaded_image_path_1)
        # 使用 cv2.split 將影像分解為 B、G、R 三個通道
        b_channel, g_channel, r_channel = cv2.split(img)

                # 分別將每個通道轉換回 BGR 圖像
        # 只有藍色通道的 BGR 圖像
        blue_image = cv2.merge([b_channel, g_channel*0, r_channel*0])

        # 只有綠色通道的 BGR 圖像
        green_image = cv2.merge([b_channel*0, g_channel, r_channel*0])

        # 只有紅色通道的 BGR 圖像
        red_image = cv2.merge([b_channel*0, g_channel*0, r_channel])

        # 顯示結果（如果您在開發環境中測試可以使用）
        cv2.imshow('Blue Channel Image', blue_image)
        cv2.imshow('Green Channel Image', green_image)
        cv2.imshow('Red Channel Image', red_image)

        # 等待按鍵並關閉視窗
        cv2.waitKey(0)
        cv2.destroyAllWindows()