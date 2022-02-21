#!/usr/bin/python

from datetime import datetime
from pprint import pprint
from my_devices import device_dict
#from getpass import getpass
from netmiko import ConnectHandler
import threading

def ssh_command(device, show_command):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command_timing(show_command)
    net_connect.disconnect()
    print(40 * '#')
    print(output)
    print(40 * '#')
    return(output)

def ssh_command2(device, show_command='show version'):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command_timing(show_command)
    net_connect.disconnect()
    return(output)

