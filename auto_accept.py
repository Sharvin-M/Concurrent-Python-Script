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


# Function to click at a specific location
def mouse_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    print("Clicked at: ", x, y)


def main():
    # Create a window to display the captured screen
    cv.namedWindow("Screen Capture", cv.WINDOW_NORMAL)
    needle_img = cv.imread("acceptButton.jpg")  # searching for accept button
    threshold = 0.5  # Threshold for confidence score
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    # continuously capture screen and search for accept button
    while True:
        # Capture the screen image
        haystack_img = capture_screen()

        # search the screen for the accept button
        result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

        # return the confidence score and position of the accept button
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        # create a bounding rectangle around the accept button
        if max_val >= threshold:
            print("Found Accept Button")
            top_left = max_loc
            bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
            cv.rectangle(
                haystack_img,
                top_left,
                bottom_right,
                color=(0, 255, 0),
                thickness=2,
                lineType=cv.LINE_4,
            )

            # click the accept button using the rectangle coordinates
            mouse_click(top_left[0] + needle_w / 2, top_left[1] + needle_h / 2)
            # don't need to display result        cv.imshow('Result', haystack_img)
            cv.waitKey()
        else:
            print("Searching for Accept Button...")
        # Break the loop if 'q' is pressed
        if cv.waitKey(1) == ord("q"):
            cv.destroyAllWindows()
            break


if __name__ == "__main__":
    main()
