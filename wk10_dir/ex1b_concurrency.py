#!/usr/bin/python

from datetime import datetime
from pprint import pprint
from my_devices import device_dict
from getpass import getpass
from netmiko import ConnectHandler

def netmiko_show(device, show_command):
    net_connect = ConnectHandler(**device)
    return(net_connect.send_command_timing(show_command))

def get_my_time():
      return(datetime.now())
  
if __name__ == '__main__':
#    pprint(device_dict)
    start_time = get_my_time()
    cmd_out_list = []
    device_list = device_dict.keys()
    my_command = 'show version'
    print(12 * '#', 'start', 12 * '#')
    for a in device_list:
        cmd_result = netmiko_show(device_dict[a], my_command)
        print(cmd_result)
        cmd_out_list.append(cmd_result)
        end_time = get_my_time() -  start_time
        print(12 * '#', end_time, (12 * '#'))

