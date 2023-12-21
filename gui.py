import customtkinter
from auto_accept import accept


def button_callback():
    accept()  # Call the accept() function from the other module


def close_callback():
    global closeButtonClicked
    closeButtonClicked = not closeButtonClicked
    app.destroy()


app = customtkinter.CTk()
app.title("Auto Accept")
app.geometry("400x150")

closeButtonClicked = False

runButton = customtkinter.CTkButton(app, text="Queue", command=button_callback)
runButton.grid(row=200, column=500, padx=20, pady=20)

closeButton = customtkinter.CTkButton(app, text="Close", command=close_callback)
closeButton.grid(row=200, column=550, padx=20, pady=20)


app.mainloop()
