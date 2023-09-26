from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, parent):
        self.parent = parent
        self.style_config()

    def find_parent_router(self):
        _current_parent = self.parent
        while True:
            if(hasattr(_current_parent, "parent_router")):
                return _current_parent
            _current_parent = _current_parent.parent

    @abstractmethod
    def style_config(self):
        ...
