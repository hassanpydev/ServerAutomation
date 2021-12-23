from core.connect import Controller
from core.response import ResponseParser


class Firewall(Controller):
    def __init__(self):
        path = "/ip/firewall/"
        super().__init__(path=path)

    def pribt_rules(self):
        return self.tuplize()
firewall = Firewall()
print(firewall.tuplize())