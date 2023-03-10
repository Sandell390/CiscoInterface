
from enum import Enum
import string
import random
import netmiko

class PortMode(Enum):
    ACCESS = 0
    TRUNK = 1
    DYNAMIC = 2

def hej():
    print("Port")


def GetPortStatus():
    connection = netmiko.ConnectHandler(ip="192.168.2.2", device_type="cisco_ios", username="cisco", password="cisco", secret="class")


    connection.enable()
    connection.send_config_set("hostname kage")
    config = connection.send_command("show run")
    connection.disconnect()
    return config


class Port:

    def __init__(self, port, state, vlan, PortMode):
        self.port = port
        self.state = state
        self.vlan = vlan
        self.mode = PortMode

    def printPortMode(self):
        print("Port Mode" + str(self.mode))
    
    

        