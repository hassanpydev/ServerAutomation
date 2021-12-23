from core.connect import Controller
from core.response import ResponseParser




class Interface(Controller):
    def __init__(self):
        self.parentMenu = "interface"
        super().__init__()

    def print_interface(self):
        return self.tuplize()


class IP(Controller):
    def __init__(self):
        self.parentMenu = "ip"
        super().__init__()

    def print_dhcp_client(self):
        path = self.api.path(*["ip", "dhcp-client"])
        return ResponseParser(self.tuplize(path)[0])

    def print_firewall_filter(self):
        path = self.api.path(*["ip", "firewall", "filter"])
        print(self.tuplize(path))
        return ResponseParser(self.tuplize(path)[0])


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


ip = IP()
print(dir(ip.print_firewall_filter()))
