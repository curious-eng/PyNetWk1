import yaml

arista1 = {
    "transport":"https",
    "host":"arista1.lasthop.io",
    "username":"pyclass",
    "port":"443",
}
arista2 = {
    "transport":"https",
    "host":"arista2.lasthop.io",
    "username":"pyclass",
    "port":"443",
}
arista3 = {
    "transport":"https",
    "host":"arista3.lasthop.io",
    "username":"pyclass",
    "port":"443",
}
arista4 = {
    "transport":"https",
    "host":"arista4.lasthop.io",
    "username":"pyclass",
    "port":"443",
}
arista_list = [{"arista1": arista1, "arista2": arista2, "arista3": arista3, "arista4": arista4}]

with open("ex4_arista.yml", "w") as f:
    yaml.dump(arista_list, f, default_flow_style=True)

