from dotenv import load_dotenv
from src.data.router import Router
from tkinter.ttk import Style
from src.styles.style import global_style_config

if __name__ == "__main__":
    load_dotenv()

    root = Router()
    global_style_config(root)
    root.show_screen("home")
    root.mainloop()

