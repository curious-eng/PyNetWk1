import yaml
from  ex4_generate_jinja_config2 import generate_jinja_config
from pprint import pprint

common_data = {
    "transport":"https",
    "username":"pyclass",
    "port":"443",
}
arista1 = {
    "hostname": "arista1",
    "host":"arista1.lasthop.io",
    "intf_name": "loopback67",
    "intf_ip": "172.31.67.41",
    "intf_mask": 30,
}
arista2 = {
    "hostname": "arista2",
    "host":"arista2.lasthop.io",
    "intf_name": "loopback68",
    "intf_ip": "172.31.68.45",
    "intf_mask": 30,
}
arista3 = {
    "hostname": "arista3",
    "host":"arista3.lasthop.io",
    "intf_name": "loopback69",
    "intf_ip": "172.31.69.49",
    "intf_mask": 30,
}
arista4 = {
    "hostname": "arista4",
    "host":"arista4.lasthop.io",
    "intf_name": "loopback70",
    "intf_ip": "172.31.70.53",
    "intf_mask": 30,
}
arista_list = [{"arista1": arista1, "arista2": arista2, "arista3": arista3, "arista4": arista4}]
config_list = []
for k, device in arista_list[0].items():
    temp_dict = {}
    arista_config = generate_jinja_config(**device)#config_list)
    temp_dict["hostname"] = device["hostname"]
    temp_dict["host"] = device["host"]
    temp_dict["data"] = arista_config.splitlines()
    for ckey, cvalue in common_data.items():
        temp_dict[ckey] = cvalue
    config_list.append(temp_dict)
#pprint(config_list)

with open("ex4_arista.yml", "w") as f:
    yaml.dump(config_list, f, default_flow_style=True)

