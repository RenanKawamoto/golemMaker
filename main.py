from src.data.router import Router
from src.screens.home import HomeScreen

if __name__ == "__main__":
    root = Router()
    root.show_screen("home")
    root.mainloop()

