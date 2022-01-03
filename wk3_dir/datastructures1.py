from pprint import pprint

arp_str = '''Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
'''
arp_lines = arp_str.splitlines()
arp_line_elements = []
for line in arp_lines:
    arp_line_elements.append(line.split())
my_dict = {}
arp_list = []
for line in arp_line_elements:
    my_dict["mac_addr"] = line[1]
    my_dict["ip_addr"] = line[3]
    my_dict["interface"] = line[5]
    arp_list.append(my_dict)
pprint(arp_list)
