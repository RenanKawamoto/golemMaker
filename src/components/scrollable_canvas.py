import tkinter as tk
from tkinter.ttk import Frame, Scrollbar, Label
from src.abstract_classes.component import Component

class ScrollableCanvas(Component, Frame):
    def __init__(self, parent, width, height):
        Component.__init__(self, parent)
        Frame.__init__(self, parent)
        
        self.canvas = tk.Canvas(self, width=width, height=height)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.vertical_scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.vertical_scrollbar.pack(side="right", fill="y", expand=True)

        self.canvas.configure(yscrollcommand=self.vertical_scrollbar.set)
        
        self.inner_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        
        for i in range(1, 100):
            label = Label(self.inner_frame, text=i)
            label.pack()

        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # Adicione eventos de rolagem do mouse
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)


    def on_mousewheel(self, event):
        # Rolar para cima
        if event.num == 4 or event.delta == 120:
            self.canvas.yview_scroll(-1, "units")
        # Rolar para baixo
        elif event.num == 5 or event.delta == -120:
            self.canvas.yview_scroll(1, "units")