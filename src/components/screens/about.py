from tkinter.ttk import Frame, Label
from src.abstract_classes.component import Component
from src.components.route_button import RouteButton
from os import getenv

class AboutScreen(Component, Frame):
    def __init__(self, parent):
        Component.__init__(self, parent)
        Frame.__init__(self, parent)
        Label(self, style="H1.TLabel",  text="Um pouco sobre o GolemMaker").place(relx=0.5, rely=0.03, anchor="n")
        Label(self, style="About.Text.TLabel", wraplength=int(getenv("WINDOW_WIDTH"))-100, justify="center",
        text="\"Este é um projeto pequeno, mas altamente eficiente, projetado com o propósito de automatizar "
        "tarefas repetitivas. Ele se destina a simplificar e agilizar a execução dessas tarefas por meio da " 
        "criação de scripts personalizados, permitindo que você economize tempo e esforço significativos no "
        "seu dia a dia\"").place(relx=0.5, rely=0.18, anchor="n")
        Label(self, style="Subtitle.TLabel", text="Criado por: Renan Kawamoto da Rocha").place(relx=0.5, rely=0.7, anchor="center")
        RouteButton(self, text="Voltar", to_where="home").place(relx=0.5, rely=0.9, anchor="s")
        
        self.local_style_config()

    def local_style_config(self):
        self.local_style.configure(
            "About.Text.TLabel",
            font=("calibri", 16, "italic")
        )