#!/usr/bin/env python

import json
from pprint import pprint

my_dict = {}
with open('arista.json', 'r') as f:
    arista_json = json.load(f)
#    pprint(arista_json)
    for my_list_element in arista_json['ipV4Neighbors']:
        my_dict[my_list_element['address']] = my_list_element['hwAddress']
        print(type(my_list_element['hwAddress']), my_list_element['hwAddress'])
#Out[7]: dict_keys(['hwAddress', 'address', 'interface', 'age'])
pprint(my_dict)

