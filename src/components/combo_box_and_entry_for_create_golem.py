from tkinter.ttk import Combobox, Label, Frame, Entry, Button
from tkinter import StringVar
from src.abstract_classes.component import Component

class ComboboxAndEntryForCreateGolem(Component, Frame):
    def __init__(self, parent):
        Component.__init__(self, parent)
        Frame.__init__(self, parent)
        
        self.combobox = Combobox(self, textvariable=self.combobox_current_option, values=self.values_in_combobox, width=self.width_combobox)
        self.combobox.grid(row=0, column=0, pady=10)

        self.combobox.bind("<<ComboboxSelected>>", self.set_fields_for_current_option)
        
    def set_fields_for_current_option(self, event):
        if self.label_x is not None:
            self.label_x.destroy()
        if self.label_y is not None:
            self.label_y.destroy()
        if self.label_time is not None:
            self.label_time.destroy()
        if self.entry_x is not None:
            self.entry_x.destroy()
        if self.entry_y is not None:
            self.entry_y.destroy()
        if self.entry_time is not None:
            self.entry_time.destroy()
        if self.label_text_const is not None:
            self.label_text_const.destroy()
        if self.entry_text_const is not None:
            self.entry_text_const.destroy()
        
        if(self.combobox_current_option.get() == "clique"):
            ...

        elif(self.combobox_current_option.get() == "mover ponteiro"):
            self.label_x = Label(self, text="X:")
            self.label_x.grid(row=0, column=1)
            
            self.entry_x = Entry(self, width=self.width_entry_x_y_time)
            self.entry_x.grid(row=0, column=2)
            
            self.label_y = Label(self, text="Y:")
            self.label_y.grid(row=0, column=3)
            
            self.entry_y = Entry(self, width=self.width_entry_x_y_time)
            self.entry_y.grid(row=0, column=4)
            
            self.label_time = Label(self, text="Tempo:")
            self.label_time.grid(row=0, column=5)
            
            self.entry_time = Entry(self, width=self.width_entry_x_y_time)
            self.entry_time.grid(row=0, column=6)

        elif(self.combobox_current_option.get() == "escrever"):
            self.label_text_const = Label(self, text="Palavra:")
            self.label_text_const.grid(row=0, column=1)

            self.entry_text_const = Entry(self, width=self.width_entry_const)
            self.entry_text_const.grid(row=0, column=2)
           

    def local_vars_set(self):
        self.values_in_combobox = ["clique", "mover ponteiro", "escrever"]
        self.width_combobox = len(max(self.values_in_combobox)) + 2
        self.width_entry_x_y_time = 4
        self.width_entry_const = 10
        self.width_trash = 2
        self.combobox_current_option = StringVar()
        self.label_x = None
        self.label_y = None
        self.label_time = None
        self.label_text_const = None
        self.entry_x = None
        self.entry_y = None
        self.entry_time = None
        self.entry_text_const = None
        