import cv2 as cv
import numpy as np



haystack_img = cv.imread("queuePop.jpg")
needle_img = cv.imread("acceptButton.jpg")


result = cv.matchTemplate(haystack_img, needle_img,  cv.TM_CCOEFF_NORMED) # method that locates needle in haystack


min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result) # returns the whitest and darkest pixels and their position
# maxVal = confidence 
# maxLoc = Location
# common practice to set a threshold for confidence 

print(max_val)
print(max_loc)