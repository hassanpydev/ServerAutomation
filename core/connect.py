import ssl
from socket import timeout
import librouteros
from librouteros import connect
import logging
from core.response import ResponseParser

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
    """
    initialize tne main connection to the router
    and return a new session object.
    """

    def __init__(self):
        try:
            self.api = connect(
                username="admin",
                password="hassan1998",
                host="192.168.8.145",
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
        """
        convert response object to tuple
        :param path: a list
        :return:
        """
        if isinstance(path, librouteros.api.Path):
            return tuple(path)
        else:
            print("Object is not tuplizable")

    def _ConvertResponseToObjectResponse(self, response):
        """
        Convert response to class with a response keys as attributes
        :return:
        """
        classes = []  # contains all classes that about to be made
        for client in self.tuplize(response):  # iterate over all response objects
            print(client)
            classes.append(
                ResponseParser(client)
            )  # convert response to class and set its attributes with response properties

        return classes
