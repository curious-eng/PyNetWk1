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
    max_procs = 4
    with ProcessPoolExecutor(max_procs) as pool:
        futures = []
#        results_generator = pool.map(ssh_command2, device_list)
        for device in network_devices:
            futures.append(pool.submit(ssh_command2, device, 'show version'))

        print('\n\n')
        for future in as_completed(futures):
            print('-' * 40)
            print('Result: ', future.result())
            print('-' * 40)
            print('\n\n')
#            end_time = datetime.now()
#            print(end_time - start_time)

       end_time = datetime.now()
       print(f'Finished in {end_time - start_time:.2f}')
       print('\n\n')
#        for result in results_genertor:
#            print(result)
#            end_time = datetime.now()
#            print(end_time - start_time)


if __name__ == '__main__':
    main_func()

