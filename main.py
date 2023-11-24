import cv2 as cv
import numpy as np
import pyautogui

haystack_img = cv.imread("queuePop.jpg")
needle_img = cv.imread("acceptButton.jpg")

# method that locates needle in haystack
result = cv.matchTemplate(haystack_img, needle_img,  cv.TM_CCOEFF_NORMED) 


min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result) 
# maxVal = confidence and maxLoc = Location
# common practice to set a threshold for confidence
print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

threshold = 0.8 
if max_val >= threshold:
    # Execute your code here if the confidence is high enough
   
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]
    
    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
    cv.rectangle(haystack_img, top_left, bottom_right, 
                 color = (0, 255, 0), thickness = 2, lineType=cv.LINE_4)
    cv.imshow('Result', haystack_img)
    cv.waitKey()
else:
    print("Needle not found")

