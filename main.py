import json
import ssl

import librouteros
from librouteros import connect, api
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.set_ciphers("ADH:@SECLEVEL=0")
api = connect(
    username="admin",
    password="hassan1998",
    host="192.168.8.140",
    ssl_wrapper=ctx.wrap_socket,
    port=8729,
)
# First create desired path.
interfaces = api.path("interface")
print(isinstance(interfaces, ))
print(type(interfaces))
system_rec = api.path("system")
# Traverse down into /interfaces/ethernet


class Controller(object):
    def __init__(self):
        self.api = connect(
            username="admin",
            password="hassan1998",
            host="192.168.8.140",
            ssl_wrapper=ctx.wrap_socket,
            port=8729,
        )


class Interface(Controller):
    def __init__(self):
        super().__init__()
        self.interfaces_path = api.path("interface")

    def print_interface(self):
        pass

    def tuplize(self):
        if isinstance(self.interfaces_path, api.path):
            return tuple(self.interfaces_path)
