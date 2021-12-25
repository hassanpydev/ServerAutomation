from typing import Iterable


class ResponseParser(object):
    """
    A class to convert api response to a class that has attributes with the same name as the response object.
    """

    def __init__(self, initial_data):
        """initialize response and set a new attributes to the class"""
        for key in initial_data:
            setattr(self, key, initial_data[key])
        self.dires = dir(self)

    def __repr__(self):
        return "A response object for %s" % self.__class__.__name__

    def __dir__(self) -> Iterable[str]:
        return [attr for attr in self.dires if not attr.startswith("_")]
