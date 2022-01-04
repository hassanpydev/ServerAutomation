from core.pathes import System


class SystemResource(System):
    def __init__(self):
        System.__init__(self)
        self.parentMenu += '/resource'
        print(self.tuplize(self.api.path(self.parentMenu)))
