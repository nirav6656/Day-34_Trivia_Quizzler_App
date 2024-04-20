THEME_COLOR = "#375362"
from tkinter import *


class app_window:
    def __init__(self):
        self.window_ui()

def window_ui():
    window = Tk()
    window.minsize(width=400,height=500)
    window.config(bg=THEME_COLOR)
    window.config(padx=50, pady=50)



    # score lable
    label = Label(text="Score: ",fg="black",background=THEME_COLOR, font=("Arial", 15, "bold"))
    label.place(anchor="w")
    label.grid(row=0,column=0)

    # canvas
    canvas = Canvas(width=300, height=300)
    quote_text = canvas.create_text(150, 90, text="Kanye Quote Goes HERE", width=300, font=("Arial", 15, "bold"),fill="black")
    canvas.grid(row=1, column=0,pady=20)



    # Button
    false_photo = PhotoImage(file="images/false.png")
    button = Button(image=false_photo)
    button.grid(row=2,column=0, sticky="e")
    true_photo = PhotoImage(file="images/true.png")
    button = Button(image=true_photo)
    button.grid(row=2, column=0, sticky="w")
    window.mainloop()