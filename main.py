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
 