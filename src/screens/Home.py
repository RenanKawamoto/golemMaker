from tkinter import Frame, Label, Button
from src.screens.About import AboutScreen

class HomeScreen(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        Label(self, text="Home").pack()
        Button(self, text="2", command=lambda:parent.showScreen(AboutScreen(parent))).pack()
