#!/usr/bin/python

from datetime import datetime
from pprint import pprint
from my_devices import device_dict
#from getpass import getpass
from netmiko import ConnectHandler
import threading
from my_functions import ssh_command2
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import time

network_devices = []
for k, v in device_dict.items():
    network_devices.append(v)

def get_my_time():
      return(datetime.now())
  
def main_func():
    """
    Use concurrent futures threading to simultaneously gather "show version" output from devices.
    Wait for all threads to complete. Record the amount of time required to do this.
    """
    start_time = time.time()
    max_threads = 5

    # Create the thread pool
    pool = ThreadPoolExecutor(max_threads)

    # Create list to append threads to
    futures = []
    for device in network_devices:
        futures.append(pool.submit(ssh_command2, device, "show version"))

    print("\n\n")
    for future in as_completed(futures):
        print("-" * 40)
        print("Result: " + future.result())
        print("-" * 40)
        print("\n\n")

    end_time = time.time()
    print(f"Finished in {end_time - start_time:.2f}")
    print("\n\n")


if __name__ == '__main__':
    main_func()

