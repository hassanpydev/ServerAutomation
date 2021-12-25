from core.connect import Controller
from core.response import ResponseParser


class Interface(Controller):
    def __init__(self):
        self.parentMenu = "interface"
        super().__init__()


class IP(Controller):
    def __init__(self):
        self.parentMenu = ["ip"]
        super().__init__()


class System(Controller):
    """
    system tab interface for accessing the submenus
    """

    def __init__(self):
        self.parentMenu = "system"
        super().__init__()


class Queue(Controller):
    """
    queue interface for accessing traffic queues
    """

    def __init__(self):
        self.parentMenu = "queue"
        super().__init__()
