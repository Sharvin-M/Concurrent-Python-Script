import customtkinter
import cv2 as cv
import numpy as np
import pyautogui

customtkinter.set_default_color_theme("dark-blue")

class AutoAcceptApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.running = False
        self.needle_img = cv.imread("acceptButton.png")
        self.threshold = 0.5
        self.needle_w = (self.needle_img).shape[1]
        self.needle_h = (self.needle_img).shape[0]

        self.title("Auto League Accept")
        self.geometry("150x150")

        self.start_button = customtkinter.CTkButton(self, text="Queue", command=self.start)
        self.stop_button = customtkinter.CTkButton(self, text="Stop", command=self.stop)
        self.quit_button = customtkinter.CTkButton(self, text="Quit", command=self.quit)

        self.start_button.grid(row=1, column=1, padx=20, pady=20)
        self.stop_button.grid(row=2, column=1, padx=20, pady=20)
        self.quit_button.grid(row=3, column=1, padx=20, pady=20)

    def capture_screen(self):
        screen_image = pyautogui.screenshot()
        frame = cv.cvtColor(np.array(screen_image), cv.COLOR_RGB2BGR)
        return frame

    def mouse_click(self, x, y):
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print("Clicked at:", x, y)

    def accept(self):
        if self.running:
            print("Searching")
            haystack_img = self.capture_screen()
            result = cv.matchTemplate(haystack_img, self.needle_img, cv.TM_CCOEFF_NORMED)
            _, _, _, max_loc = cv.minMaxLoc(result)

            if result[max_loc[1], max_loc[0]] >= self.threshold:
                print("Found Accept Button")
                top_left = max_loc
                self.mouse_click(top_left[0] + self.needle_w / 2, top_left[1] + self.needle_h / 2)
            self.after(105, self.accept)

    def start(self):
        self.running = True
        print("Started")
        self.accept()

    def stop(self):
        self.running = False
        print("Stopped")

    def quit(self):
        self.running = False
        print("Quit")
        self.destroy()

if __name__ == "__main__":
    app = AutoAcceptApp()
    app.mainloop()

