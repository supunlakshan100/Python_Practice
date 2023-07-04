class Person:
    def __init__(self, name):
        super().__init__()
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
