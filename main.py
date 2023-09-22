from src.data.Router import Router
from src.screens.Home import HomeScreen

if __name__ == "__main__":
    root = Router()
    root.showScreen("Home")
    root.mainloop()

