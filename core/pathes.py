from core.connect import Controller


class IP(Controller):
    def __init__(self):
        super().__init__(path="ip")

    def __truediv__(self, other):
        return self.api.path(self.path.join(other))

    def __repr__(self):
        return self.path


i = IP()
new_path = IP() / "addresses"
print(new_path.tuplize())
