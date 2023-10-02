from tkinter.ttk import Label, Frame
from src.abstract_classes.component import Component
from src.components.route_button import RouteButton
from os import getenv

class HomeScreen(Component, Frame):
    def __init__(self, parent):
        Component.__init__(self, parent)
        Frame.__init__(self, parent)
        Label(self, text="Golem Maker", style="Title.H1.TLabel").place(relx=0.5, rely=0, anchor="n")
        RouteButton(self, text="Sobre", to_where="about").place(relx=0.5, rely=0.9, anchor="s")

    def local_style_config(self):
        self.local_style.configure(
            "Title.H1.TLabel",
            foreground = getenv("THIRD_COLOR"),
            font=("Josefin Sans", 35, "bold")
        )