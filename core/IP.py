from core import IP, ResponseParser


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
        self.dhcpClientInfo = {}
        for i in dir(self.clients):
            if i == "status" and self.clients.__getattribute__(i) == "searching...":
                self.dhcpClientInfo.update({"address": "None"})
                self.dhcpClientInfo.update({"expires_after": "00:00:00"})
            self.dhcpClientInfo.update({i: self.clients.__getattribute__(i)})


class BaseAddressesTap(IP):
    """
    An interface for retrieving addresses
    """

    def __init__(self):
        super().__init__()
        self.parentMenu += "/address"

    def All_Addresses(self) -> list:
        addresses = self._ConvertResponseToObjectResponse(
            self.api.path(self.parentMenu)
        )
        return addresses


class Addresses:
    def __init__(self, address_o):
        self.address_o = address_o
        self.AddressesInfo = {}
        for i in dir(self.address_o):
            self.AddressesInfo.update({i: self.address_o.__getattribute__(i)})


class DNS(IP):
    """
    An interface to interact with DNS data.
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


class Firewall(IP):
    def __init__(self):
        super().__init__()
        self.parentMenu += "/firewall"

    def AllRules(self, rules):
        return self._ConvertResponseToObjectResponse(rules)


class NAT_Rules(Firewall):
    def __init__(self):
        super().__init__()
        self.parentMenu += "/nat"
        _rules = self.AllRules(self.api.path(self.parentMenu))
        for rule in _rules:
            print("Rule", dir(rule))


class FilterRules(Firewall):
    def __init__(self):
        super().__init__()
        self.parentMenu += "/filter"
        _rules = self.AllRules(self.api.path(self.parentMenu))
        for rule in _rules:
            print("Rule", dir(rule))


class Routes(IP):
    def __init__(self):
        super().__init__()
        self.parentMenu += "/route"
        _route = self._ConvertResponseToObjectResponse(self.api.path(self.parentMenu))
        for route in _route:
            print("Route", dir(route))
