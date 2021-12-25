from core import IP


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


class DNS(IP):
    def __init__(self):
        super().__init__()
        self.parentMenu.append("dns")
        self.dns = self.api.path(*self.parentMenu)
        self.dns_response = self.ConvertResponseToObjectResponse(self.dns)[0]
        print(dir(self.dns_response))
