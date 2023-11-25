import cv2 as cv
import numpy as np
import pyautogui

# Function to capture the entire screen
def capture_screen():
    # Get the screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Capture the screen image
    screen_image = pyautogui.screenshot()

    # Convert the image to OpenCV format
    frame = cv.cvtColor(np.array(screen_image), cv.COLOR_RGB2BGR)

    return frame

# Create a window to display the captured screen
cv.namedWindow('Screen Capture', cv.WINDOW_NORMAL)
needle_img = cv.imread("acceptButton.jpg")
threshold = 0.5 
needle_w = needle_img.shape[1]
needle_h = needle_img.shape[0]

# Continuously capture the screen and display it
while True:
    # Capture the screen image
    haystack_img = capture_screen()

    result = cv.matchTemplate(haystack_img, needle_img,  cv.TM_CCOEFF_NORMED) 
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result) 

    if max_val >= threshold:
        # Execute your code here if the confidence is high enough
        print("Found needle") 
        top_left = max_loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
        cv.rectangle(haystack_img, top_left, bottom_right, 
                    color = (0, 255, 0), thickness = 2, lineType=cv.LINE_4)
        cv.imshow('Result', haystack_img)
        cv.waitKey()
    else:
        print("Needle not found")
    # Break the loop if 'q' is pressed
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break