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

def get_my_time():
      return(datetime.now())
  
def main_func():
    start_time = datetime.now()
    for k, v in device_dict.items():
        my_thread = threading.Thread(target=ssh_command, args=(v, 'show version'))
        my_thread.start()
    main_thread = threading.currentThread()
    for a_thread in threading.enumerate():
        print(12 * ':', 'thread name: ', a_thread, 12 * ':')
        if a_thread != main_thread:
            a_thread.join()    
            print(12 * '#', ' execution time: ', datetime.now() - start_time, 12 * '#')

if __name__ == '__main__':
    main_func()

