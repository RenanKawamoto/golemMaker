from tkinter import ttk
from src.abstract_classes.component import Component

class Button2(Component, ttk.Button):
    def __init__(self, parent, text):
        self.style = ttk.Style()
        self.style.theme_use("default")
        Component.__init__(self, parent)
        ttk.Button.__init__(
                self, 
                parent, 
                text=text, 
                command=lambda: self.find_parent_router().show_screen(to_where),
        )

    def local_style_config(self):
        self.style.configure(
                "TButton", 
                background="white"
        )
