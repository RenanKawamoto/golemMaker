from tkinter import Tk

class Router(Tk):
    def __init__(self):
        super().__init__()
        self.title("Golem Maker")
        self.geometry("500x500")
        self.resizable(False, False)
        self.currentScreen = None

    def showScreen(self):
        if self.currentScreen:
            self.currentScreen.destroy()

        self.currentScreen = screen
        self.currentScreen.pack()



