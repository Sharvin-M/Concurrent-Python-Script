import cv2 as cv
import numpy as np
import pyautogui
import threading

cv.namedWindow("Screen Capture", cv.WINDOW_NORMAL)
needle_img = cv.imread("acceptButton.jpg")  # searching for accept button
threshold = 0.5  # Threshold for confidence score
needle_w = needle_img.shape[1]
needle_h = needle_img.shape[0]


def capture_screen():
    screen_width, screen_height = pyautogui.size()
    screen_image = pyautogui.screenshot()
    frame = cv.cvtColor(np.array(screen_image), cv.COLOR_RGB2BGR)
    return frame


def mouse_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    print("Clicked at: ", x, y)


def main():
    found = False
    while not found:
        haystack_img = capture_screen()
        result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if max_val >= threshold:
            found = True
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
            mouse_click(top_left[0] + needle_w / 2, top_left[1] + needle_h / 2)
        else:
            print("Searching for Accept Button...")


thread_main = threading.Thread(target=main)
thread_capture_screen = threading.Thread(target=capture_screen, daemon=True)

all_threads = [
    thread_main,
    thread_capture_screen,
]
for th in all_threads:
    th.start()

main()
