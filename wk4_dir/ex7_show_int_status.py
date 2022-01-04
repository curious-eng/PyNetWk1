import textfsm
from pprint import pprint

template_file = "ex2_show_interface_status.template"
template = open(template_file)

with open("ex2_show_interface_status.txt") as f:
    raw_text_data = f.read()

import ipdb
ipdb.set_trace

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)

template.close()

my_list= []
my_dict = {}
for my_line in data:
    my_dict['DUPLEX'] = my_line[3]
    my_dict['PORT_NAME'] = my_line[0]
    my_dict['PORT_TYPE'] = my_line[5]
    my_dict['SPEED'] = my_line[4]
    my_dict['STATUS'] = my_line[1]
    my_dict['VLAN'] = my_line[2]
    my_list.append(my_dict)
    my_dict = {}
#    print(my_line)

pprint(my_list)

#[['Gi0/1/0', 'notconnect', '1', 'auto', 'auto', '10/100/1000BaseTX'],
# ['Gi0/1/1', 'notconnect', '1', 'auto', 'auto', '10/100/1000BaseTX'],
# ['Gi0/1/2', 'notconnect', '1', 'auto', 'auto', '10/100/1000BaseTX'],
# ['Gi0/1/3', 'notconnect', '1', 'auto', 'auto', '10/100/1000BaseTX']]
#
