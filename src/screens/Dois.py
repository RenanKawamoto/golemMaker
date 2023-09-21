from tkinter import Frame, Label

class DoisScreen(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        Label(self, text="2").pack()
