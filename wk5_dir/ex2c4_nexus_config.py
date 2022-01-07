import json

############ define new config #############
nxos1_new_conf = {
    "sw_name": "nxos1",
    "interface": "Ethernet1/1",
    "as_no": 22,
}
nxos2_new_conf = {
    "sw_name": "nxos2",
    "interface": "Ethernet1/1",
    "as_no": 22,
}
############ define list ############
my_list = [nxos1_new_conf, nxos2_new_conf]

############ write it to a file ###########
filename = 'ex2f_nexus_config.json'
with open(filename, 'w') as f:
    f.write(json.dumps(my_list))

#########################################################
