import customtkinter
from auto_accept import accept

def button_callback():
    accept()  # Call the accept() function from the other module

<<<<<<< HEAD

def close_callback():
    global closeButtonClicked
    closeButtonClicked = not closeButtonClicked
    app.destroy()
=======
# def close_callback():
    # app.destroy()
>>>>>>> parent of 0f96fad (fix: close button functionality)


app = customtkinter.CTk()
app.title("Auto Accept")
app.geometry("400x150")

<<<<<<< HEAD
closeButtonClicked = False

runButton = customtkinter.CTkButton(app, text="Queue", command=button_callback)
runButton.grid(row=200, column=500, padx=20, pady=20)

closeButton = customtkinter.CTkButton(app, text="Close", command=close_callback)
closeButton.grid(row=200, column=550, padx=20, pady=20)
=======
button = customtkinter.CTkButton(app, text="In Queue", command=button_callback)
button.grid(row=200, column=500, padx=20, pady=20)
>>>>>>> parent of 0f96fad (fix: close button functionality)


app.mainloop()
