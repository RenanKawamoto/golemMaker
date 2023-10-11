from tkinter.ttk import Button
from src.abstract_classes.component import Component

class RouteButton(Component, Button):
    def __init__(self, parent, text, to_where):
        Component.__init__(self, parent)
        Button.__init__(
                self, 
                parent, 
                text=text, 
                command=lambda: self.find_parent_router().show_screen(to_where),
                style="RouteButton.TButton"
        )
        
        self.local_style_config()

    def local_style_config(self):
        self.local_style.configure(
            "RouteButton.TButton",
            font=("Josefin Sans", 25, "bold")
        )
