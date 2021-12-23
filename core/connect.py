import ssl

import librouteros
from librouteros import connect

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.set_ciphers("ADH:@SECLEVEL=0")


def MakePath(path):
    ...


class Controller(object):
    def __init__(self, path):

        self.api = connect(
            username="admin",
            password="hassan1998",
            host="192.168.8.140",
            ssl_wrapper=ctx.wrap_socket,
            port=8729,
        )

        self.path = self.api.path(path)

    def tuplize(self):
        if isinstance(self.path, librouteros.api.Path):
            return tuple(self.path)
