#!/usr/bin/python

from datetime import datetime
from pprint import pprint
from my_devices import device_dict, device_list
#from getpass import getpass
from netmiko import ConnectHandler
import threading
from my_functions import ssh_command2
from concurrent.futures import ThreadPoolExecutor, wait, as_completed, ProcessPoolExecutor

def get_my_time():
      return(datetime.now())
  
def main_func():
    start_time = datetime.now()
    max_threads = 4
    with ProcessPoolExecutor(max_threads) as pool:
        results_generator = pool.map(ssh_command2, device_list)
        for my_output in as_completed(results_generator):
            print('Result: ', my_output.result())
            end_time = datetime.now()
            print(end_time - start_time)

#        for result in results_genertor:
#            print(result)
#            end_time = datetime.now()
#            print(end_time - start_time)


if __name__ == '__main__':
    main_func()

