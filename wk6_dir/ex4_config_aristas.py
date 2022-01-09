from getpass import getpass
from my_funcs2 import read_yaml,  send_config_to_arista

command = "show ip arp"
config = ["interface loopback 0", "description JB"]
devices = read_yaml("ex4_arista.yml")
password = getpass()
for k, dev in devices[0].items():
    print(k)
    dev["password"] = password
    output = send_config_to_arista(dev, config)
    print(output)

