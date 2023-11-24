import cv2 as cv
import pyautogui
import numpy as np

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

# Continuously capture the screen and display it
while True:
    # Capture the screen image
    screen_image = capture_screen()

    # Display the captured screen image
    cv.imshow('Screen Capture', screen_image)

    # Break the loop if 'q' is pressed
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
