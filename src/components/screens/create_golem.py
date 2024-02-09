from tkinter import StringVar
from tkinter.ttk import Frame, Label, Button, Entry
from src.abstract_classes.component import Component
from src.components.route_button import RouteButton
from src.components.scrollable_canvas import ScrollableCanvas
from src.components.label_and_entry import LabelAndEntry
from src.components.combo_box_and_entry_for_create_golem import ComboboxAndEntryForCreateGolem

import pyautogui

class CreateGolemScreen(Component, Frame):    
    def __init__(self, parent):
        Component.__init__(self, parent)
        Frame.__init__(self, parent)
        
        self.label_x_y = Label(self, text=f"", style="xY.TLabel")
        self.label_x_y.place(relx=0.3, rely=0.0, anchor="ne")         
        
        self.label_and_entry = LabelAndEntry(self, label_text="Nome do golem: ", text_variable=self.file_name, entry_width=self.entry_file_name_width)
        self.label_and_entry.place(relx=0.866, rely=0.1, anchor="ne")
      
        self.scrollable_canvas = ScrollableCanvas(self, width=self.scrollable_canvas_width, height=self.scrollable_canvas_height)
        self.scrollable_canvas.place(relx=0.5, rely=0.15, anchor="n")
             
        #self.scrollable_canvas.add_component_in_canvas_grid(Button, row=self.current_row+1, column=1, text="Adicionar comando +", command=self.create_command_row, width=self.button_add_command_width)
        #self.scrollable_canvas.add_component_in_canvas_grid(Button, row=self.current_row+2, column=0, text="X", command=self.delete_last_command_row, width=self.button_delete_command_width)
        
        self.route_button_home = RouteButton(self, text="Voltar", to_where="golem")
        self.route_button_home.place(relx=0.25, rely=0.95, anchor="s")
        
        self.button_create = Button(self, text="Criar", style="Create.TButton", command=lambda:print(self.file_name.get()))
        self.button_create.place(relx=0.75, rely=0.95, anchor="s")
                        
        self.define_x_y()           
        self.local_style_config()
          
    def define_x_y(self):
        x, y = pyautogui.position()
        self.label_x_y.config(text=f"x: {x} y: {y}")
        self.label_x_y.after(10, self.define_x_y)
    
    def create_command_row(self):
        self.current_row += 1
        self.scrollable_canvas.add_component_in_canvas_grid(Button, row=self.current_row+1, column=1, text="Adicionar comando +", command=self.create_command_row, width=self.button_add_command_width)
        self.scrollable_canvas.add_component_in_canvas_grid(ComboboxAndEntryForCreateGolem, row=self.current_row, column=0)
    
    def delete_last_command_row(self):
        self.scrollable_canvas.remove_component_in_canvas_grid(row=self.current_row, column=1)
        self.scrollable_canvas.remove_component_in_canvas_grid(row=self.current_row, column=1)
        self.current_row -= 1
        print(self.current_row)

    def local_style_config(self):
        #self.entry_file_name.configure(width=100)
        self.local_style.configure(
            "Create.TButton",
            font=("Josefin Sans", 25, "bold")
        )
        self.local_style.configure(
            "xY.TLabel",
            font=("Josefin Sans", 15)
        )
        
    def local_vars_set(self):
        self.file_name = StringVar()
        self.teste = StringVar()
        self.current_row = 0

        self.scrollable_canvas_width = 350
        self.scrollable_canvas_height = 300
        self.entry_file_name_width = 44
        self.button_add_command_width = 26
        self.button_delete_command_width = 8