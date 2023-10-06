from tkinter import Canvas
from tkinter.ttk import Frame, Scrollbar, Button
from src.abstract_classes.component import Component
from os import getenv

class ScrollableCanvas(Component, Frame):
    def __init__(self, parent, width, height):
        Component.__init__(self, parent)
        Frame.__init__(self, parent)
        self.canvas = Canvas(self, width=width, height=height)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.vertical_scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.vertical_scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.vertical_scrollbar.set)
        
        self.inner_frame = Frame(self.canvas, style="InnerFrame.TFrame")
        
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)	
        
        self.local_style_config()
      
        
      
    def add_component_in_canvas(self, component, *args, **kwargs):
        _component = component(self.inner_frame, *args, **kwargs)
        _component.pack(side="top", fill="x", expand=True)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.update_idletasks()

    def on_mousewheel(self, event):
        if event.delta == 120:
            self.canvas.yview_scroll(-1, "units")
        elif event.delta == -120:
            self.canvas.yview_scroll(1, "units")

    def local_style_config(self):
        self.canvas.configure(bg=getenv("SECOND_COLOR"),  highlightthickness  = 0)