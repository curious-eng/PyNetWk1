#!/usr/bin/env python

from netmiko import ConnectHandler
import yaml
from pprint import pprint

with open('/home/jbrooker/.netmiko.yml', 'r') as f:
    devices = yaml.safe_load(f)

net_connect = ConnectHandler(**devices['cisco3'])
print(net_connect.find_prompt())

