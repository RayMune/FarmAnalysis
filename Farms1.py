import cv2
import numpy as np

def classify_soil_or_vegetation(image_path):

    img=cv2.imread(image_path)

    #convert to hsv clor space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Define color ranges for soil and veg
    soil_lower = np.array([0, 0, 100])
    soil_upper = np.array([40, 255, 255])
    green_lower = np.array([40, 50, 50])
    green_upper = np.array([80, 255, 255])

    #create mask for soil and veg
    mask_soil = cv2.inRange(hsv, soil_lower, soil_upper)
    mask_green= cv2.inRange(hsv, green_lower, green_upper)

    #calc % pixels
    soil_ratio=cv2.countNonZero(mask_soil) / (img.shape[0] * img.shape[1])
    green_ratio=cv2.countNonZero(mask_green) / (img.shape[0] * img.shape[1])

    #classify
    if soil_ratio > green_ratio:
        return "soil"
    else:
        return "vegetation"
    
image_path = "C:\\Users\\USER\\Downloads\\FarmImage.png"

classification = classify_soil_or_vegetation(image_path)
print(f"Image classified as: {classification}")

