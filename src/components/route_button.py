from tkinter import ttk
from src.abstract_classes.component import Component

class RouteButton(Component, ttk.Button):
    def __init__(self, parent, text, to_where):
        Component.__init__(self, parent)
        ttk.Button.__init__(
                self, 
                parent, 
                text=text, 
                command=lambda: self.find_parent_router().show_screen(to_where),
                style="RouteButton.TButton"
        )

    def style_config(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure("RouteButton.TButton")
