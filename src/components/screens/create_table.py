from tkinter.ttk import Label, Frame
from src.abstract_classes.component import Component
from src.components.route_button import RouteButton
from os import getenv
from src.components.label_and_entry import LabelAndEntry

class CreateTableScreen(Component, Frame):
    def __init__(self, parent):
        Component.__init__(self, parent)
        Frame.__init__(self, parent)
             
        Label(self, text="Criar tabela:", style="Title.H1.TLabel").place(relx=0.5, rely=0, anchor="n")
        self.label_and_entry = LabelAndEntry(self, label_text="Nome da tabela: ", text_variable=self.table_name, entry_width=self.entry_table_name_width)
        self.label_and_entry.place(relx=0.866, rely=0.15, anchor="ne")
        RouteButton(self, text="Voltar", to_where="table").place(relx=0.5, rely=0.9, anchor="s")
        
        self.local_style_config()
   
    def local_style_config(self):
        self.local_style.configure(
            "Title.H1.TLabel",
            foreground = getenv("THIRD_COLOR"),
            font=("Josefin Sans", 35, "bold")
        )
        
    def local_vars_set(self):
        self.table_name = ""
        self.entry_table_name_width = 44