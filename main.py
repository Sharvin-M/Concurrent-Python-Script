import cv2 as cv
import numpy as np



haystack_img = cv.imread("queuePop.jpg", cv.IMREAD_UNCHANGED)
needle_img = cv.imread("acceptButton.jpg", cv.IMREAD_UNCHANGED)


result = cv.matchTemplate(haystack_img, needle_img,  cv.TM_CCOEFF_NORMED) # method that locates needle in haystack


cv.imshow('Result', result) # script
cv.waitKey() # pauses script
