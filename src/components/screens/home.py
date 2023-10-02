from tkinter.ttk import Label, Frame
from src.abstract_classes.component import Component
from src.components.route_button import RouteButton

class HomeScreen(Component, Frame):
    def __init__(self, parent):
        Component.__init__(self, parent)
        Frame.__init__(self, parent)
        Label(self, text="Home").pack()
        RouteButton(self, text="Sobre", to_where="sobre").place(relx=0.5, rely=1, anchor="s")
