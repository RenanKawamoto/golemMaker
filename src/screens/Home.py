from tkinter import Frame, Label, Button

class HomeScreen(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        Label(self, text="Home").pack()
        Button(self, text="About", command=lambda: parent.showScreen("About")).pack()
