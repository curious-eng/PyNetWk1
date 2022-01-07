import json

############ define new config #############
nxos1_new_conf = {
    "sw_name": "nxos1",
    "interface": "Ethernet1/1",
    "ip_addr": "10.1.100.1",
    "netmask": 24,
    "as_no": 22,
    "neighbor_ip": "10.1.100.2",
}
nxos2_new_conf = {
    "sw_name": "nxos2",
    "interface": "Ethernet1/1",
    "ip_addr": "10.1.100.2",
    "netmask": 24,
    "as_no": 22,
    "neighbor_ip": "10.1.100.1",
}
############ define list ############
my_list = [nxos1_new_conf, nxos2_new_conf]

############ write it to a file ###########
filename = 'ex2e_nexus_config.txt'
with open(filename, 'w') as f:
    f.write(json.dumps(my_list))

#########################################################
