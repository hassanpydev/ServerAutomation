from core import *

# all_dhcp = BaseDHCPClient()
# for dhcp in all_dhcp.AllDHCPClientS():
#     dhcpclient = DHCPClient(clients=dhcp)
#     for key, value in dhcpclient.dhcpClientInfo.items():
#
#         print("{}={}".format(key, value))
#     # print("DHCP dhcpServer", dhcpclient.dhcpServer())
#     # print("DHCP status", dhcpclient.dhcpClientStatus())
#     # print("DHCP addresses", dhcpclient.addresses())
#     # print("DHCP isDefaultRoute", dhcpclient.isDefaultRoute())
#     # print("DHCP DHCPInterface", dhcpclient.DHCPInterface())
#     # print("DHCP dhcpClientGateway", dhcpclient.DHCPClientGateway())
#     # print("DHCP dhcpClientPrimary_dns", dhcpclient.DHCPClientPrimary_dns())
#     # print("DHCP DHCPClientExpiresAfter", dhcpclient.DHCPClientExpiresAfter())
#     print("=" * 20)
# all_addresses = BaseAddressesTap()
# for address in all_addresses.All_Addresses():
#     address_info = Addresses(address_o=address)
#     # iterate over dictionary and print keys and values
#     for key, value in address_info.AddressesInfo.items():
#
#         print("{}={}".format(key, value))
#     print(" " * 20)
from core.System import SystemResource

rules = Routes()
