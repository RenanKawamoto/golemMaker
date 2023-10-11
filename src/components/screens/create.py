from tkinter import StringVar
from tkinter.ttk import Frame, Label, Button, Entry
from src.abstract_classes.component import Component
from src.components.route_button import RouteButton
from src.components.scrollable_canvas import ScrollableCanvas
from src.components.label_and_entry import LabelAndEntry

class CreateScreen(Component, Frame):
    def __init__(self, parent):
        Component.__init__(self, parent)
        Frame.__init__(self, parent)
      
        self.scrollable_canvas_width = 350
        self.scrollable_canvas_height = 300
        self.entry_file_name_width = 44
             
             
        self.label_and_entry = LabelAndEntry(self, label_text="Nome do golem: ", text_variable=self.file_name, entry_width=self.entry_file_name_width)
        self.label_and_entry.place(relx=0.866, rely=0.1, anchor="ne")
      
        self.scrollable_canvas = ScrollableCanvas(self, width=self.scrollable_canvas_width, height=self.scrollable_canvas_height)
        self.scrollable_canvas.place(relx=0.5, rely=0.15, anchor="n")
        self.scrollable_canvas.add_component_in_canvas_grid(Button, row=self.current_row, column=0, text="+", command=self.create_command)
        
        self.route_button_home = RouteButton(self, text="Voltar", to_where="home")
        self.route_button_home.place(relx=0.25, rely=0.95, anchor="s")
        
        self.button_create = Button(self, text="Criar", style="Create.TButton", command=lambda:print(self.file_name.get()))
        self.button_create.place(relx=0.75, rely=0.95, anchor="s")
                
        self.local_style_config()
          
    def create_command(self):
        self.current_row += 1  
        self.scrollable_canvas.add_component_in_canvas_grid(Button, row=self.current_row, column=0, text="+", command=self.create_command)
    
    def local_style_config(self):
        #self.entry_file_name.configure(width=100)
        self.local_style.configure(
            "Create.TButton",
            font=("Josefin Sans", 25, "bold")
        )
        
    def local_vars_set(self):
        self.file_name = StringVar()
        self.current_row = 0
        