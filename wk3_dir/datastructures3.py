#!/usr/bin/env python

import json
from pprint import pprint

ipv4_list = []
ipv6_list = []

with open('NAPALM_nxos_ssh.json', 'r') as f:
    napalm_json = json.load(f)
#    pprint(napalm_json)
    for my_key1 in napalm_json.keys():
        for my_key2 in napalm_json[my_key1].keys():
            for my_key3 in napalm_json[my_key1][my_key2].keys():
                if my_key2 == 'ipv4':
                    ipv4_list.append(my_key3 + '/' + str(napalm_json[my_key1][my_key2][my_key3]['prefix_length']))
                elif my_key2 == 'ipv6':
                    ipv6_list.append(my_key3 + '/' + str(napalm_json[my_key1][my_key2][my_key3]['prefix_length']))
print()
print('ipv4 list:')
pprint(ipv4_list)
print()
print('ipv6 list:')
pprint(ipv6_list)
print()

data = {
 'Ethernet2/1': {'ipv4': {'1.1.1.1': {'prefix_length': 24}}},
 'Ethernet2/2': {'ipv4': {'2.2.2.2': {'prefix_length': 27},
                          '3.3.3.3': {'prefix_length': 25}}},
 'Ethernet2/3': {'ipv4': {'4.4.4.4': {'prefix_length': 16}},
                 'ipv6': {'2001:db8::1': {'prefix_length': 10},
                          'fe80::2ec2:60ff:fe4f:feb2': {'prefix_length': 64}}},
 'Ethernet2/4': {'ipv6': {'2001:11:2233::a1': {'prefix_length': 24},
                          '2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2': {'prefix_length': 64},
                          'fe80::2ec2:60ff:fe4f:feb2': {'prefix_length': 64}}}
}

#output:
#ipv4 list:
#['1.1.1.1/24', '2.2.2.2/27', '3.3.3.3/25', '4.4.4.4/16']

#ipv6 list:
#['fe80::2ec2:60ff:fe4f:feb2/64',
# '2001:db8::1/10',
# 'fe80::2ec2:60ff:fe4f:feb2/64',
# '2001:11:2233::a1/24',
# '2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2/64']

