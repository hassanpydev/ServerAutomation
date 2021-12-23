from core.connect import Controller
from core.response import ResponseParser


class Interface(Controller):
    def __init__(self):
        self.interfaces_path = "interface"
        super().__init__(path=self.interfaces_path)

    def print_interface(self):
        return self.tuplize()


interface = Interface()
print(interface.print_interface()[0])
