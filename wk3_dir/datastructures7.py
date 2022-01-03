#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
from netmiko import ConnectHandler
import yaml
from pprint import pprint

bgp_config = '''router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
'''.splitlines()

cisco_obj = CiscoConfParse(bgp_config)
bgp_neighbours = cisco_obj.find_objects_w_child(parentspec=r'^router bgp', childspec=r'^ neighbor \d')# bgp_neighbors is the list of CiscoConfParse objects containing the neighbours
print(bgp_neighbours, bgp_neighbours[0])# returns: [<IOSCfgLine # 0 'router bgp 44'>] <IOSCfgLine # 0 'router bgp 44'>
my_neighbors = bgp_neighbours[0].re_search_children(r'neighbor')# my_neighbors is the list of ciscoConfParse 'neighbour' children
print(my_neighbors)# returns: [<IOSCfgLine # 4 ' neighbor 10.220.88.20' (parent is # 0)>, <IOSCfgLine # 12 ' neighbor 10.220.88.32' (parent is # 0)>]
print()
my_list = []
for n in my_neighbors:
    a = n.text.split()[1]# n.text returns a list where [1] is the IP address
    print(n.text)# returns:  neighbor 10.220.88.20 (1st time around)
    b = n.re_search_children(r'remote-as')[0].text.split()[1]# n.re_search_children(r'remote-as') returns a list where [0].text is 'remote-as 42' split creats a list where [1] is the AS
    print(n.re_search_children(r'remote-as'))# returns: [<IOSCfgLine # 5 '  remote-as 42' (parent is # 4)>] (1st time around)
    my_list.append((a,b))
    print()
#
#[<IOSCfgLine # 0 'router bgp 44'>] <IOSCfgLine # 0 'router bgp 44'>
#[<IOSCfgLine # 4 ' neighbor 10.220.88.20' (parent is # 0)>, <IOSCfgLine # 12 ' neighbor 10.220.88.32' (parent is # 0)>]
#
# neighbor 10.220.88.20
#[<IOSCfgLine # 5 '  remote-as 42' (parent is # 4)>]
#
# neighbor 10.220.88.32
#[<IOSCfgLine # 13 '  remote-as 43' (parent is # 12)>]
#

