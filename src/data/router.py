from os import getenv
from tkinter import Tk, ttk
import json

class Router(Tk):
    def __init__(self):
        super().__init__()
        self.parent_router = self
        with open(getenv("SCREENS_LIST_PATH")) as file:
            self.screens_list = json.load(file)
        self.title("Golem Maker")
        self.geometry(getenv("WINDOW_WIDTH")+"x"+getenv("WINDOW_HEIGHT"))
        self.resizable(False, False)
        self.current_screen = None
        self.style = ttk.Style(self)
        self.style.configure("TButton", background="blue")

    def show_screen(self, screen_name):
        if self.current_screen:
            self.current_screen.destroy()
        
        if screen_name in self.screens_list:
            default_path = "src.components.screens."
            screen_name_class = self.screens_list[screen_name] + "Screen"

            import_screen_file = __import__(default_path + screen_name, fromlist=[screen_name_class])
            class_screen = getattr(import_screen_file, screen_name_class)
            self.current_screen = class_screen(self)
            self.current_screen.pack(fill="both", expand=True)
