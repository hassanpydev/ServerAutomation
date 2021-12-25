from core.connect import Controller
from core.response import ResponseParser
from core.IP import DHCPClient

dhcp = DHCPClient()
print(dir(dhcp.getDhcpClientAsClasses()[0]))
print(dhcp.getDhcpClientAsClasses()[0].comment)
