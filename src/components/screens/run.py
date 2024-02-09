from tkinter.ttk import Frame, Label
from src.abstract_classes.component import Component
from src.components.route_button import RouteButton

class RunScreen(Component, Frame):
    def __init__(self, parent):
        Component.__init__(self, parent)
        Frame.__init__(self, parent)
        Label(self, text="Rodar").pack()
        RouteButton(self, text="Voltar", to_where="golem").pack()