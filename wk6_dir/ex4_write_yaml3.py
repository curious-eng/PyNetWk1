import yaml

arista1 = {
    "hostname": "arista1",
    "host":"arista1.lasthop.io",
    "transport":"https",
    "username":"pyclass",
    "port":"443",
    "data": {
        "intf_name": "loopback67",
        "intf_ip": "172.31.67.41",
        "intf_mask": 30,
    }
}
arista2 = {
    "hostname": "arista2",
    "host":"arista2.lasthop.io",
    "transport":"https",
    "username":"pyclass",
    "port":"443",
    "data": {
        "intf_name": "loopback68",
        "intf_ip": "172.31.68.45",
        "intf_mask": 30,
    }
}
arista3 = {
    "hostname": "arista3",
    "host":"arista3.lasthop.io",
    "transport":"https",
    "username":"pyclass",
    "port":"443",
    "data": {
        "intf_name": "loopback69",
        "intf_ip": "172.31.69.49",
        "intf_mask": 30,
    }
}
arista4 = {
    "hostname": "arista4",
    "host":"arista4.lasthop.io",
    "transport":"https",
    "username":"pyclass",
    "port":"443",
    "data": {
        "intf_name": "loopback70",
        "intf_ip": "172.31.70.53",
        "intf_mask": 30,
    }
}
arista_list = [{"arista1": arista1, "arista2": arista2, "arista3": arista3, "arista4": arista4}]

with open("ex4_devices.yml", "w") as f:
    yaml.dump(arista_list, f, default_flow_style=True)

