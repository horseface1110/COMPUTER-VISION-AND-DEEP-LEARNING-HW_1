import cv2, globals
import numpy as np
from Sobel_X import Sobel_X
from Sobel_Y import Sobel_Y
import matplotlib.pyplot as plt

def Combination_and_Threshold():
    if not globals.loaded_image_path_1 :
        print("請先輸入圖片_1")
        return
    image = cv2.imread(globals.loaded_image_path_1, cv2.IMREAD_GRAYSCALE) 
    
    # Apply Sobel X and Y
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # Sobel X
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Sobel Y

    # Compute the combination of Sobel X and Y
    combined = np.sqrt(sobelx**2 + sobely**2)

    # Normalize the result to 0–255
    normalized = cv2.normalize(combined, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    # Apply thresholding with two different thresholds
    _, threshold_128 = cv2.threshold(normalized, 128, 255, cv2.THRESH_BINARY)
    _, threshold_28 = cv2.threshold(normalized, 28, 255, cv2.THRESH_BINARY)

    # Display the images
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.title('Combination of Sobel X and Y')
    plt.imshow(normalized, cmap='gray')
    plt.subplot(1, 3, 2)
    plt.title('Threshold = 128')
    plt.imshow(threshold_128, cmap='gray')
    plt.subplot(1, 3, 3)
    plt.title('Threshold = 28')
    plt.imshow(threshold_28, cmap='gray')
    plt.show()