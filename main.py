from time import sleep

from core.connect import Controller
from core.response import ResponseParser
from core import Interface
def convert_bytes(size):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

    return size
interface = Interface()
print(dir(interface.AllInterfaces()[0]))
print(interface.AllInterfaces()[0])
while True:
    eth0 = interface.AllInterfaces()[0]
    print("Speed is:",convert_bytes(eth0.tx_byte))
    sleep(1)

"""'actual_mtu', 'default_name', 'dires', 'disabled', 'fp_rx_byte', 'fp_rx_packet',
 'fp_tx_byte', 'fp_tx_packet', 'last_link_up_time', 'link_downs', 'mac_address',
 'mtu', 'name', 'running', 'rx_byte', 'rx_drop', 'rx_error', 'rx_packet', 'tx_byte',
  'tx_drop', 'tx_error', 'tx_packet', 'tx_queue_drop', 'type'] """