from tkinter.ttk import Frame, Label, Button, Entry
from src.abstract_classes.component import Component
from src.components.route_button import RouteButton
from src.components.scrollable_canvas import ScrollableCanvas

class CreateScreen(Component, Frame):
    def __init__(self, parent):
        Component.__init__(self, parent)
        Frame.__init__(self, parent)
        
        self.entry_file_name = Entry(self, textvariable=self.file_name, width=self.entry_file_name_width)
        self.entry_file_name.place(relx=0.866, rely=0.113, anchor="ne")
        
        scrollable_canvas = ScrollableCanvas(self, width=self.scrollable_canvas_width, height=self.scrollable_canvas_height)
        scrollable_canvas.place(relx=0.5, rely=0.15, anchor="n")
        
        RouteButton(self, text="Voltar", to_where="home").place(relx=0.25, rely=0.95, anchor="s")
        Button(self, text="Criar", style="Create.TButton").place(relx=0.75, rely=0.95, anchor="s")
        
        self.local_style_config()
        
    def local_style_config(self):
        #self.entry_file_name.configure(width=100)
        self.local_style.configure(
            "Create.TButton",
            font=("Josefin Sans", 25, "bold")
        )
        
    def local_vars_set(self):
        self.file_name = ""
        self.scrollable_canvas_width = 350
        self.scrollable_canvas_height = 300
        self.entry_file_name_width = 40