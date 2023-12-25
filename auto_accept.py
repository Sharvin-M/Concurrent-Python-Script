import customtkinter
import cv2 as cv
import numpy as np
import pyautogui


customtkinter.set_default_color_theme("dark-blue")


running = None


def capture_screen():
    screen_width, screen_height = pyautogui.size()
    screen_image = pyautogui.screenshot()
    frame = cv.cvtColor(np.array(screen_image), cv.COLOR_RGB2BGR)
    return frame


def mouse_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    print("Clicked at: ", x, y)


def accept():
    cv.namedWindow("Screen Capture", cv.WINDOW_NORMAL)
    needle_img = cv.imread("acceptButton.jpg")
    threshold = 0.5
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]
    print("began search")
    if running:
        haystack_img = capture_screen()
        result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        if max_val >= threshold:
            print("Found Accept Button")
            top_left = max_loc
            mouse_click(top_left[0] + needle_w / 2, top_left[1] + needle_h / 2)
        app.after(100, accept)


def start():
    global running
    running = True
    accept()


def stop():
    global running
    running = False
    print("stopped")


def quit():
    global running
    running = False
    print("quit")
    app.destroy()


app = customtkinter.CTk()
app.title("Auto League Accept")
app.geometry("400x150")

startButton = customtkinter.CTkButton(app, text="Queue", command=start)
stopButton = customtkinter.CTkButton(app, text="Stop", command=stop)
quitButton = customtkinter.CTkButton(app, text="Quit", command=quit)

startButton.grid(row=1, column=1, padx=20, pady=20)
stopButton.grid(row=2, column=1, padx=20, pady=20)
quitButton.grid(row=3, column=1, padx=20, pady=20)

app.after(100, accept)
app.mainloop()
