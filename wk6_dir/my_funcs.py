import yaml
from getpass import getpass
import pyeapi

def read_yaml(filename, my_command):
    with open(filename, "r") as f: 
        arista = yaml.safe_load(f)
    arista['password'] = getpass()
# enable = getpass("Enable: ")
# device = pyeapi.client.Node(connection. enablepwd=enable)
    connection = pyeapi.client.connect(**arista)
    device = pyeapi.client.Node(connection)
    return(device.enable(my_command))
    

def print_show_arp(data):
    for ip in data[0]['result']['ipV4Neighbors']:
        print(ip['address'] + ' --> ' + ip['hwAddress'])

if __name__=='__main__':
    output = read_yaml("ex2a_arista4.yml","show ip arp")
    print_show_arp(output)

 

