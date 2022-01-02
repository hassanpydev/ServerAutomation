from core import *

all_dhcp = BaseDHCPClient()
for dhcp in all_dhcp.AllDHCPClientS():
    dhcpclient = DHCPClient(clients=dhcp)
    print("DHCP client",dhcpclient.dhcpServer())