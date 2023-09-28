from tkinter.ttk import Frame, Label
from src.abstract_classes.component import Component
from src.components.route_button import RouteButton

class SobreScreen(Component, Frame):
    def __init__(self, parent):
        Component.__init__(self, parent)
        Frame.__init__(self, parent)
        Label(self, text="Um pouco sobre o MakeGolem").pack()
        Label(self, text="Um pequeno projeto que tem o intuito de optimizar tarefas repetitivas criando scripts para faze-las.\n Criado por: Renan Kawamoto da Rocha").pack()
        RouteButton(self, text="Voltar", to_where="home").pack()

    def local_style_config(self):
        ...
