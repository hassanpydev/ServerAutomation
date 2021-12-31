from core import IP


class BaseDHCPClient(IP):
    """
    a base class for retrieving dhcp client information.
    """

    def __init__(self):
        super().__init__()
        self.parentMenu += (
            "/dhcp-client"  # change path to dhcp-client instead of IP path
        )

    def AllDHCPClientS(self):
        dhcpClient = self._ConvertResponseToObjectResponse(
            self.api.path(self.parentMenu)
        )  # retrieve all dhcp-client data
        return dhcpClient


class DHCPClient:
    def __init__(self, clients):
        self.clients = clients

    def isDefaultRoute(self):
        return self.clients.add_default_route

    def addresses(self):
        return self.clients.address

    def dhcpServer(self):
        return self.clients.dhcp_server

    def dhcpClientStatus(self):
        return self.clients.status


class DNS(IP):
    """
    A interface to interact with DNS data.
    """

    def __init__(self):
        super().__init__()
        self.parentMenu += "/dns"
        self.dns = self.api.path(self.parentMenu)
        self.dns_response = self._ConvertResponseToObjectResponse(self.dns)[0]

    def Cache(self):
        """
        a method to retrieve dns cache records.
        :return: list of cache records.
        """
        self.parentMenu += "/cache"
        cache = self.api.path(self.parentMenu)
        return self._ConvertResponseToObjectResponse(cache)

    def Static(self):
        """
        a method to retrieve static dns records
        :return: list of static dns records.
        """
        self.parentMenu += "/static"

        static = self.api.path(*self.parentMenu)
        return self._ConvertResponseToObjectResponse(static)
