
from pprint import pprint
from jnpr.junos import Device
from getpass import getpass

a_device = Device(host="srx2.lasthop.io", user="pyclass", password=getpass())
a_device.open()
pprint(a_device.facts)
print()
print("hostname:  {}".format(a_device.facts['hostname']))
