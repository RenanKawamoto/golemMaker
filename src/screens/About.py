from tkinter import Frame, Label, Button
from src.screens.Home import HomeScreen

class AboutScreen(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        Label(self, text="About").pack()
        Button(self, text="Home", command=lambda: parent.showScreen(HomeScreen(parent)))
