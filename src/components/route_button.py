from tkinter.ttk import Button
from src.abstract_classes.component import Component

class RouteButton(Component, Button):
    def __init__(self, parent, text, to_where, text_size=15, padding=5, background_color="#9A3B3B", text_color="white"):
        self._background_color = background_color
        self._text_color = text_color
        self._text_size = text_size
        self._padding = padding

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
