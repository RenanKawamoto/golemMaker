class Component():
    def __init__(self, parent):
        self.parent = parent

    def find_parent_router(self):
        _current_parent = self.parent
        while True:
            if(hasattr(_current_parent, "parent_router")):
                return _current_parent
            _current_parent = _current_parent.parent
