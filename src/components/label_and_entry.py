from tkinter.ttk import Entry, Label, Frame
from src.abstract_classes.component import Component

class LabelAndEntry(Component, Frame):
    def __init__(self, parent, label_text, text_variable, entry_width):
        Component.__init__(self, parent)
        Frame.__init__(self, parent)
        
        self.label = Label(self, text=label_text)
        self.label.grid(row=0, column=0)
        
        self.entry = Entry(self, textvariable=text_variable, width=entry_width)
        self.entry.grid(row=0, column=1)                      
