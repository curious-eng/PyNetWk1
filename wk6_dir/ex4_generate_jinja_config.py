from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates"])

arista1 = {
    "hostname": "arista1",
    "intf_name": "loopback67",
    "intf_ip": "172.31.67.41",
    "intf_mask": 30,
}
arista2 = {
    "hostname": "arista2",
    "intf_name": "loopback68",
    "intf_ip": "172.31.68.45",
    "intf_mask": 30,
}
arista3 = {
    "hostname": "arista3",
    "intf_name": "loopback69",
    "intf_ip": "172.31.69.49",
    "intf_mask": 30,
}
arista4 = {
    "hostname": "arista4",
    "intf_name": "loopback70",
    "intf_ip": "172.31.70.53",
    "intf_mask": 30,
}

my_list = [arista1, arista2, arista3, arista4]

template_file = 'ex4_arista_config.j2'
template = env.get_template(template_file)

config_list = []
for arista_device in my_list:
    config = ""
    config = template.render(**arista_device)
    config_list.append(config)
pprint(config_list)

