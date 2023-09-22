from tkinter.ttk import Button, Style

class GenericButton(Button):
    def __init__(self, parent, text, command, fontSize):
        style = Style()
        style.configure("Generic.TButton", font=("Calibri", fontSize, "bold"), padding=5)

        super().__init__(parent, text=text, command=command, style="Generic.TButton")


