from tkinter import Frame, Label, Button

class AboutScreen(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        Label(self, text="About").pack()
        Button(self, text="Home", command=lambda: parent.showScreen("Home")).pack()
