from core import BaseInterfaces, EthernetInterfaces


def convert_bytes(size):
    for x in ["bytes", "KB", "MB", "GB", "TB"]:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

    return size


interface = BaseInterfaces(int_path="ethernet")
for inter in interface.AllInterfaces():
    try:
        inte = EthernetInterfaces(inter)
        print("Mac Address", inte.interfaceMACAddress)
        print("interface Name", inte.interfaceName)
        print("interfaceStatus", inte.interfaceStatus)
        print("interfaceSpeed", inte.InterfaceSpeed)
        print("InterfaceTotalReceivedPacket", inte.InterfaceTotalReceivedPacket)
        print("InterfaceTotalSentPacket", inte.InterfaceTotalSentPacket)
        print("InterfaceIsLoopProtected", inte.InterfaceIsLoopProtected)
        print("**" * 15)
    except AttributeError:
        print("Error: Unknown attributes")

"""'actual_mtu', 'default_name', 'disabled', 'fp_rx_byte', 'fp_rx_packet',
 'fp_tx_byte', 'fp_tx_packet', 'last_link_up_time', 'link_downs', 'mac_address',
 'mtu', 'name', 'running', 'rx_byte', 'rx_drop', 'rx_error', 'rx_packet', 'tx_byte',
  'tx_drop', 'tx_error', 'tx_packet', 'tx_queue_drop', 'type'] """
