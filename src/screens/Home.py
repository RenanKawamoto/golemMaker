from tkinter import Frame, Label, Button, ttk
from src.components.GenericButton import GenericButton


class HomeScreen(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        Label(self, text="Home").pack()
        GenericButton(self, text="BotaoGenerico", command=lambda:print("ola"), fontSize=20).pack()
        Button(self, text="About", command=lambda: parent.showScreen("About")).pack()
        ttk.Button(self, text="ola").pack()
