from core.connect import Controller
from core.response import ResponseParser


class BaseInterfaces(Controller):
    """
    A base class for retrieveing interfaces and convert them into interfaces object.
    :usage:
    >>> inter = BaseInterfaces()
    >>> inter.AllInterfaces()

    """

    def __init__(self, int_path: str):
        self.parentMenu = "interface/" + int_path.strip()
        super().__init__()

    def AllInterfaces(self, activeOnly: bool = False) -> list:
        """
        methods to return all interfaces on server
        :type activeOnly: bool
        :param activeOnly: return all active interfaces
        :return: a list of all interfaces
        """
        interfaces = self._ConvertResponseToObjectResponse(
            self.api.path(self.parentMenu)
        )
        if activeOnly:
            return [inter for inter in interfaces if inter.get("disabled") != True]
        else:
            return interfaces


class EthernetInterfaces:
    """
    A class that deals with interfaces individually.

    """

    __slots__ = "interface"

    def __init__(self, interface):
        self.interface = interface

    @property
    def interfaceStatus(self):
        return "Disabled" if self.interface.disabled else "Active"

    @property
    def InterfaceSpeed(self):
        return self.interface.speed

    @property
    def InterfaceIsLoopProtected(self):
        return "No" if self.interface.loop_protect_status == "off" else "Yes"

    @property
    def InterfaceTotalReceivedPacket(self):
        return self.interface.rx_packet

    @property
    def InterfaceTotalSentPacket(self):
        return self.interface.tx_packet

    @property
    def interfaceMACAddress(self):
        return self.interface.mac_address

    @property
    def interfaceLinkDownCounter(self):
        return self.interface.link_downs

    @property
    def interfaceLastTimeUp(self):
        return self.interface.last_link_up_time

    @property
    def interfaceName(self):
        return self.interface.name

    @property
    def interfaceType(self):
        return "Ethernet"


class IP(Controller):
    def __init__(self):
        self.parentMenu = "ip"
        super().__init__()


class System(Controller):
    """
    system tab interface for accessing the submenus
    """

    def __init__(self):
        self.parentMenu = "system"
        super().__init__()


class Queue(Controller):
    """
    queue interface for accessing traffic queues
    """

    def __init__(self):
        self.parentMenu = "queue"
        super().__init__()
