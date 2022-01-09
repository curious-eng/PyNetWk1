import yaml
from getpass import getpass
import pyeapi

def read_yaml(filename):
    with open(filename, "r") as f: 
        return(yaml.safe_load(f))

def send_cmd_to_arista(arista, my_command):
#    arista['password'] = getpass()
# enable = getpass("Enable: ")
# device = pyeapi.client.Node(connection. enablepwd=enable)
    connection = pyeapi.client.connect(**arista)
    device = pyeapi.client.Node(connection)
    return(device.enable(my_command))
    
#def send_config_to_arista(arista, my_config):
def send_config_to_arista(**arista):
# enable = getpass("Enable: ")
# device = pyeapi.client.Node(connection. enablepwd=enable)
    connection = pyeapi.client.connect(**arista)
    device = pyeapi.client.Node(connection)
    return(device.config(arista['data']))

def print_show_arp(data):
    for ip in data[0]['result']['ipV4Neighbors']:
        print(ip['address'] + ' --> ' + ip['hwAddress'])

if __name__=='__main__':
    device = read_yaml("ex2a_arista4.yml")
    print(device)
    device['password'] = getpass()
    out2 = send_cmd_to_arista(device, "show ip arp")
    print_show_arp(out2)

 

