#!/usr/bin/env python
#from jnpr_devices import srx2
from pprint import pprint
from jnpr.junos import Device
from getpass import getpass
from jnpr_devices import srx2
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.routes import RouteTable

def check_connected(a_device):
    return(a_device.connected)
# - Verify that your NETCONF connection is working. You can use the .connected attribute to check the status of this connection.

def gather_routes(a_device):
    return(RouteTable(a_device))
# - Return the routing table from the device.
#routes  RouteTable         get-route-information          show route

def gather_arp_table(a_device):
    return(ArpTable(a_device))
# - Return the ARP table from the device.
#arp  ArpTable  get-arp-table-information  show arp

def print_output(a_device, arps, routes):
    print("hostname: {}".format(a_device.facts["hostname"]))
    print("NETCONF port: {}".format(a_device.port))
    print("username: {}".format(a_device.user))
    #print("routing table")
    for item in arps.keys():
        print("IP: {} MAC: {}".format(arps[item]["ip_address"], arps[item]['mac_address']))
    for item in routes.keys():
        print("{} via {}".format(item, routes[item]['nexthop']))
# - A function that takes the Juniper PyEZ Device object, the routing table, and the ARP 
#
a_device = Device(**srx2)
a_device.open()
if check_connected(a_device):
    routes = gather_routes(a_device).get()
#    print(routes)
    arps = gather_arp_table(a_device).get()
#    print(arps)
    print_output(a_device, arps, routes)
#arp  ArpTable  get-arp-table-information  show arp
#routes  RouteTable         get-route-information          show route
#        RouteSummaryTable  get-route-summary-information  show route summary
#
#In [13]: routes.items()
#Out[13]:
#[('0.0.0.0/0',
#  [('protocol', 'Static'),
#   ('via', 'vlan.0'),
#   ('age', 19430911),
#   ('nexthop', '10.220.88.1')]),
# ('10.220.88.0/24',
#  [('protocol', 'Direct'),
#   ('via', 'vlan.0'),
#   ('age', 19430911),
#   ('nexthop', None)]),
# ('10.220.88.42/32',
#  [('protocol', 'Local'),
#   ('via', 'vlan.0'),
#   ('age', 19430925),
#   ('nexthop', None)])]
#
#In [14]: arps.get()
#Out[14]: ArpTable:srx2.lasthop.io: 3 items
#
#In [15]: arps.items()
#Out[15]:
#[('00:62:ec:29:70:fe',
#  [('mac_address', '00:62:ec:29:70:fe'),
#   ('ip_address', '10.220.88.1'),
#   ('interface_name', 'vlan.0')]),
# ('00:01:00:ff:00:01',
#  [('mac_address', '00:01:00:ff:00:01'),
#   ('ip_address', '10.220.88.37'),
#   ('interface_name', 'vlan.0')]),
# ('00:02:00:ff:00:01',
#  [('mac_address', '00:02:00:ff:00:01'),
#   ('ip_address', '10.220.88.38'),
#   ('interface_name', 'vlan.0')])]
#
