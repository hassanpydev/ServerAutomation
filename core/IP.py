from core import ResponseParser, IP


class DHCPClient(IP):
    #
    def __init__(self):
        super().__init__()
        self.parentMenu.append(
            "dhcp-client"
        )  # change path to dhcp-client instead of IP path
        self.dhcpClient = self.api.path(
            *self.parentMenu
        )  # retrieve all dhcp-client data

    def getDhcpClientAsClasses(self):
        """
        get addresses that are being taken from the DHCP server
        :return:
        """
        clients = []  # contains all dhcp clients
        for client in self.tuplize(self.dhcpClient):  # iterate over all dhcp clients
            clients.append(
                ResponseParser(client)
            )  # convert client to class and set its attributes with dhcp properties

        return clients
