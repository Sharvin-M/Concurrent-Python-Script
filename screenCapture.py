import cv2 as cv
import numpy as np
import pyautogui
import cv2 as cv
import numpy as np
import pygetwindow as gw
import win32gui
import win32ui

# Function to capture the entire screen
def capture_screen():
    # Get the screen dimensions
    screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

    # Create a device context
    hdesktop = win32gui.GetDesktopWindow()
    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)

    # Create a compatible bitmap
    compatible_bitmap = win32ui.CreateBitmap()
    compatible_bitmap.CreateCompatibleBitmap(img_dc, screen_width, screen_height)

    # Select the compatible bitmap into the device context
    img_dc.SelectObject(compatible_bitmap)

    # Copy the screen into the compatible bitmap
    img_dc.BitBlt((0, 0), (screen_width, screen_height), img_dc, (0, 0), win32con.SRCCOPY)

    # Convert the bitmap to an image
    bmp_info = compatible_bitmap.GetInfo()
    bmp_str = compatible_bitmap.GetBitmapBits(True)
    screen_image = np.frombuffer(bmp_str, dtype='uint8').reshape((bmp_info['bmHeight'], bmp_info['bmWidth'], 4))

    # Release the device context
    img_dc.DeleteDC()
    win32gui.ReleaseDC(hdesktop, desktop_dc)

    return screen_image

# Create a window to display the captured screen
cv.namedWindow('Screen Capture', cv.WINDOW_NORMAL)

# Continuously capture the screen and display it
while True:
    # Capture the screen image
    screen_image = capture_screen()

    # Convert the image to OpenCV format
    frame = cv.cvtColor(screen_image, cv.COLOR_BGRA2RGB)

    # Display the captured screen image
    cv.imshow('Screen Capture', frame)

    # Break the loop if 'q' is pressed
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
