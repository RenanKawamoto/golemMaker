from tkinter.ttk import Frame, Label
from src.abstract_classes.component import Component
from src.components.route_button import RouteButton

class AboutScreen(Component, Frame):
    def __init__(self, parent):
        Component.__init__(self, parent)
        Frame.__init__(self, parent)
        Label(self, text="About").pack()
        RouteButton(self, text="Home", to_where="home").pack()

    def local_style_config(self):
        ...
