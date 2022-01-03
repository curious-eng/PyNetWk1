#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
from netmiko import ConnectHandler
import yaml
from pprint import pprint

with open('/home/jbrooker/.netmiko.yml', 'r') as f:
    devices = yaml.safe_load(f)
devices['cisco4']['session_log'] = 'log.log'#’my_session.txt’
net_connect = ConnectHandler(**devices['cisco4'])#, session_log=’my_session.txt’)
get_show_run = net_connect.send_command('show run').splitlines()
#print(type(get_show_run))

cisco_obj = CiscoConfParse(get_show_run)
intf = cisco_obj.find_objects_w_child(parentspec=r'^interface', childspec=r'ip address \d')
for i in  intf:
    print()
    print('Interface Line: ' + i.text)
    print('IP address Line:' + i.re_search_children(r'ip address')[0].text)
    print()
#my_commands = ['interface loopback 0', 'ip address 10.192.1.1 255.255.255.255', 'no shut']
#net_connect.send_config_set(my_commands)
net_connect.send_config_set('no interface loopback 0')


