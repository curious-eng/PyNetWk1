#!usr/bin/env/ python

from my_devices import device_dict
from napalm import get_network_driver

def make_napalm_connection(device_name):
    device_type = device_dict[device_name].pop('device_type')
    driver = get_network_driver(device_type)
    return(driver(**device_dict[device_name]))

a_device = make_napalm_connection('cisco3')

