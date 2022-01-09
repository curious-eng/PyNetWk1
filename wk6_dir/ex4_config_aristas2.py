from getpass import getpass
from my_funcs2 import read_yaml,  send_config_to_arista

#command = "show ip arp"
#config = ["interface loopback 0", "description JB"]
def config_aristas(filename): 
    devices = read_yaml(filename)
    password = getpass()
    for k, dev in devices[0].items():
#        print(k, dev)#data ['interface loopback67', '  ip address 172.31.67.41/30']
        dev["password"] = password
        dev["session_log"] = k + '.log'
        output = send_config_to_arista(**dev)
        print(output)

if __name__ == "__main__":
    config_aristas('ex4_arista.yml')

