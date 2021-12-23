import ssl
from socket import timeout
import librouteros
from librouteros import connect
import logging

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.set_ciphers("ADH:@SECLEVEL=0")
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="myapp.log",
    filemode="+a",
)


class Controller(object):
    def __init__(self):
        try:
            self.api = connect(
                username="admin",
                password="hassan1998",
                host="192.168.8.142",
                ssl_wrapper=ctx.wrap_socket,
                port=8729,
                timeout=3,
            )
            logging.info("Connection created successfully to server")
        except timeout as e:
            logging.error("Connection timed out while trying to connect")
            exit(-1)

    @staticmethod
    def tuplize(path):
        if isinstance(path, librouteros.api.Path):
            return tuple(path)
        else:
            print("Object is not tuplizable")
