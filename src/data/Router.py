from tkinter import Tk
import json

class Router(Tk):
    def __init__(self):
        super().__init__()
        with open("src/screens/screensList.json") as file:
            self.screensList = json.load(file)
        self.title("Golem Maker")
        self.geometry("500x500")
        self.resizable(False, False)
        self.currentScreen = None

    def showScreen(self, screenName):
        if self.currentScreen:
            self.currentScreen.destroy()
        
        if screenName in self.screensList:
            defaultPath = "src.screens."
            screenNameClass = self.screensList[screenName] + "Screen"

            importScreenFile = __import__(defaultPath + self.screensList[screenName], fromlist=[screenNameClass])
            classScreen = getattr(importScreenFile, screenNameClass)
            self.currentScreen = classScreen(self)
            self.currentScreen.pack()
