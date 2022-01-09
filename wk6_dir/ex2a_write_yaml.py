import yaml

arista4 = {
    "transport":"https",
    "host":"arista4.lasthop.io",
    "username":"pyclass",
    "port":"443",
}

with open("ex2a_arista.yml", "w") as f:
    yaml.dump(arista4, f, default_flow_style=True)

