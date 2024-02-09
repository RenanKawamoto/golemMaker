from tkinter.ttk import Label, Frame
from src.abstract_classes.component import Component
from src.components.route_button import RouteButton
from os import getenv

class TableScreen(Component, Frame):
    def __init__(self, parent):
        Component.__init__(self, parent)
        Frame.__init__(self, parent)
             
        Label(self, text="Tabelas:", style="Title.H1.TLabel").place(relx=0.5, rely=0, anchor="n")
        RouteButton(self, text="Criar", to_where="create_table").place(relx=0.5, rely=0.3, anchor="s")
        
        RouteButton(self, text="Voltar", to_where="home").place(relx=0.5, rely=0.9, anchor="s")
        
        self.local_style_config()
   
    def local_style_config(self):
        self.local_style.configure(
            "Title.H1.TLabel",
            foreground = getenv("THIRD_COLOR"),
            font=("Josefin Sans", 35, "bold")
        )