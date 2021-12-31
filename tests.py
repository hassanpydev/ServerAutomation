
from core import *

client = Controller()
dns = DNS()
dhcp = BaseDHCPClient()
for i in dhcp.AllDHCPClientS():
    dhcpc = DHCPClient(clients=i)
    print(dhcpc.dhcpServer())
    print(dhcpc.isDefaultRoute())
    print(dhcpc.addresses())
    print(dhcpc.dhcpClientStatus())