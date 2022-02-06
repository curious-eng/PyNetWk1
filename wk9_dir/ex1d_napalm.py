#!usr/bin/env/ python

from my_devices import device_dict
from napalm import get_network_driver
from pprint import pprint

def make_napalm_connection(**dev_dict):#device_name):
    device_type = dev_dict.pop('device_type')
    print(device_type)
    pprint(dev_dict)
    driver = get_network_driver(device_type)
    return(driver(**dev_dict))

#a_device = make_napalm_connection('cisco3')

connection_object_list = []
#pprint(device_dict)
for k, v in device_dict.items():
    connection_object_list.append(make_napalm_connection(**v))

for a in connection_object_list:
    print('connection object:', a)
    a.open()
    my_facts = a.get_facts()
    print('device facts:')
    pprint(my_facts)
    print('NAPALM platform type:', a.platform)
    a.close()

