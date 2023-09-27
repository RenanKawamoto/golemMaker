from tkinter.ttk import Label, Frame
from src.abstract_classes.component import Component
from src.components.route_button import RouteButton

class HomeScreen(Component, Frame):
    def __init__(self, parent):
        Component.__init__(self, parent)
        Frame.__init__(self, parent)
        Label(self, text="Home").pack()
        RouteButton(self, text="About", to_where="about").pack()

    def local_style_config(self):
        ...
