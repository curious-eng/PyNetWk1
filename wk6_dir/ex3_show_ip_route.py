from pprint import pprint
from my_funcs import read_yaml

def print_show_ip_route(data):
    for route, network in data[0]['result']['vrfs']['default']['routes'].items():
        if network['routeType'] == 'static':
            print(route + ' type: ' + network['routeType'] + ', next hop: ' + network['vias'][0]['nexthopAddr'])
        elif network['routeType'] == 'connected':
            print(route + ' type: ' + network['routeType'])


if __name__=='__main__':
    filename = 'ex2a_arista4.yml'
    my_command = 'show ip route'
    output = read_yaml(filename, my_command)
    print_show_ip_route(output)

