from tkinter.ttk import Frame, Label, Button
from src.abstract_classes.component import Component
from src.components.route_button import RouteButton
from src.components.scrollable_canvas import ScrollableCanvas

class CreateScreen(Component, Frame):
    def __init__(self, parent):
        Component.__init__(self, parent)
        Frame.__init__(self, parent)
        Label(self, text="Create").pack()
        
        scrollable_canvas = ScrollableCanvas(self, width=350, height=300)
        scrollable_canvas.place(relx=0.5, rely=0.15, anchor="n")
 
        RouteButton(self, text="Voltar", to_where="home").place(relx=0.25, rely=0.95, anchor="s")
        Button(self, text="Criar", style="Create.TButton").place(relx=0.75, rely=0.95, anchor="s")
        
        self.local_style_config()
        
    def local_style_config(self):
        self.local_style.configure(
            "Create.TButton",
            font=("Josefin Sans", 25, "bold")
        )
        
        