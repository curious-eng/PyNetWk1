from pprint import pprint
import yaml
from netmiko import ConnectHandler

with open('devices.yml', 'r') as f:
    dev_list = yaml.safe_load(f)

#dev_index = 0
#for dev in dev_list:
#    pprint(dir(dev))

dir_list = ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

for dev in dev_list:
#    print(dev.items())
#    print(dev.keys())
#    print(dev.values())
#    print('*' *12)
#    print(dev)
    if dev['device_type'] == 'cisco_ios':
        dev['username'] = '<insert real username>'
        dev['password'] = '<insert real pasword>'
        dev.__delitem__('device_name')
        print(type(dev))
        net_connect = ConnectHandler(**dev)
        command = 'show version'
        output = net_connect.send_command(command)
        print(output)

