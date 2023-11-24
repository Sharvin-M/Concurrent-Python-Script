import cv2 as cv
import numpy as np
import pyautogui

# Set the screen capture dimensions
screen_width, screen_height = pyautogui.size()
screen_capture_region = (0, 0, screen_width, screen_height)

# Create a window to display the captured screen
cv.namedWindow('Screen Capture', cv.WINDOW_NORMAL)

# Continuously capture the screen and display it
while True:
    # Capture the screen image
    screen_image = pyautogui.screenshot(region=screen_capture_region)
    
    # Convert the image to OpenCV format
    frame = np.array(screen_image)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    
    # Display the captured screen image
    cv.imshow('Screen Capture', frame)
    
    # Break the loop if 'q' is pressed
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break