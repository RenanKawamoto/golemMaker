from abc import ABC, abstractmethod
from tkinter.ttk import Style

class Component(ABC):
    def __init__(self, parent):
        self.parent = parent
        self.local_style = Style()

    def find_parent_router(self):
        _current_parent = self.parent
        while True:
            if(hasattr(_current_parent, "parent_router")):
                return _current_parent
            _current_parent = _current_parent.parent

    def local_style_config(self):
        ...