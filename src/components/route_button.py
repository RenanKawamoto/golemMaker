from tkinter import ttk
from src.abstract_classes.component import Component

class RouteButton(Component, ttk.Button):
    def __init__(self, parent, text, to_where, text_size=15, padding=5, background_color="#9A3B3B", text_color="white"):
        self.style = ttk.Style()
        self.style.theme_use("default")
        self._background_color = background_color
        self._text_color = text_color
        self._text_size = text_size
        self._padding = padding

        Component.__init__(self, parent)
        ttk.Button.__init__(
                self, 
                parent, 
                text=text, 
                command=lambda: self.find_parent_router().show_screen(to_where),
                style="RouteButton.TButton"
        )

    def style_config(self):
        self.style.configure(
                "RouteButton.TButton", 
                background=self._background_color,
                foreground=self._text_color,
                font=("calibri", self._text_size),
                padding=self._padding
        )
