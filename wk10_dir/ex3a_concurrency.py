#!/usr/bin/python

from datetime import datetime
from pprint import pprint
from my_devices import device_dict
#from getpass import getpass
from netmiko import ConnectHandler
import threading
from my_functions import ssh_command2
from concurrent.futures import ThreadPoolExecutor, wait

def get_my_time():
      return(datetime.now())
  
#def main_func():
#    start_time = datetime.now()
#    for k, v in device_dict.items():
#        my_thread = threading.Thread(target=ssh_command, args=(v, 'show version'))
#        my_thread.start()
#    main_thread = threading.currentThread()
#    for a_thread in threading.enumerate():
#        print(12 * ':', 'thread name: ', a_thread, 12 * ':')
#        if a_thread != main_thread:
#            a_thread.join()    
#            print(12 * '#', ' execution time: ', datetime.now() - start_time, 12 * '#')

def main_func():
    start_time = datetime.now()
    max_threads = 4
    pool = ThreadPoolExecutor(max_threads)
    future_list = []
    for k, v in device_dict.items():
        future = pool.submit(ssh_command2, v)
        future_list.append(future)
    wait(future_list)
    end_time = datetime.now()
    print(12 * '#', 'duration: ', end_time - start_time, 12 * '#')
    pprint(future_list)

if __name__ == '__main__':
    main_func()

