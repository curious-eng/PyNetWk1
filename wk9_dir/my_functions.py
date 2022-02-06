#!usr/bin/env/ python

from my_devices import device_dict
from napalm import get_network_driver
from pprint import pprint
from datetime import datetime

def open_napalm_connection(**dev_dict):
    #accepts dict where k,v are hostname, device connection dict, specifically device_dict from my_devices.py
    device_type = dev_dict.pop('device_type')
    driver = get_network_driver(device_type)
    return(driver(**dev_dict))

def do_napalm_getter(conn_obj, getter_requested=""):
    try:
        conn_obj.open()
    except:
        print('***************** an error occurred trying to open the device *****************')
    if getter_requested not in dir(conn_obj):
        print('***************** unsupported getter *****************')
    if getter_requested == 'get_arp_table':
        try:
            print()
            print(conn_obj.get_facts()['hostname'])
#            import ipdb
#            ipdb.set_trace()
#            hit_enter()
            pprint(conn_obj.get_arp_table())
        except:
            print('***************** an error occurred trying to get arp table *****************')
    if getter_requested == 'get_ntp_peers':
        try:
            print()
            print(conn_obj.get_facts()['hostname'])
#            import ipdb
#            ipdb.set_trace()
#            hit_enter()
            pprint(conn_obj.get_ntp_peers())
        except:
            print('***************** an error occurred trying to get ntp peers **************    ***')

def create_backup(conn_obj):
    try:
        conn_obj.open()
    except:
        print('***************** an error occurred trying to open the device *****************')
    try:
        my_config = conn_obj.get_config()
    except:
        print('***************** an error occurred trying to retrieve the config *****************')
    dt_iso = datetime.now().isoformat().replace(':', '.')
    cfg_filename = conn_obj.get_facts()['hostname'] + '-config_backup-' + dt_iso
    print(cfg_filename)
    print(type(my_config),my_config.keys())
    #print(my_config)
    with open(cfg_filename, 'w') as f:
        f.write(my_config['running'])

def config_merge_napalm(conn_obj, config_file_name):
    try:
        conn_obj.open()
    except:
        print('***************** an error occurred trying to open the device *****************')
    try:
        conn_obj.load_merge_candidate(filename=config_file_name)
        print('config differencies before commit:\n', conn_obj.compare_config())
    except:
        print('***************** an error occurred trying to load or compare the config *****************')
    hit_enter()
    print('commit: ', conn_obj.commit_config())
    print('config differencies after commit:\n', conn_obj.compare_config())
    hit_enter()

def hit_enter():
    input('Hit enter to continue: ')

def create_checkpoint(conn_obj):
    checkpoint_file = ''
    print(conn_obj.hostname)
    try:
        conn_obj.open()
    except:
        print('***************** an error occurred trying to open the device *****************')
    try:
        checkpoint_file = conn_obj._get_checkpoint_file()
        dt_iso = datetime.now().isoformat().replace(':', '.')
        cfg_filename = conn_obj.get_facts()['hostname'] + '-checkpoint-' + dt_iso
        with open(cfg_filename, 'w') as f:
            f.write(checkpoint_file)
        print('checkpoint written to file: ', cfg_filename)
    except:
        print('***************** an error occurred trying to create the checkpoint or discard the chnge *****************')

def restore_checkpoint(conn_obj, checkpoint_file):
    try:
        conn_obj.open()
        conn_obj.load_replace_candidate(filename=checkpoint_file)
        print(conn_obj.hostname)
        print('compare before commit: ', conn_obj.compare_config())
        hit_enter()
        print('discard config:')
        conn_obj.discard_config()
        print('compare after discard: ', conn_obj.compare_config())

    except:
        print('*************** an error occurred in restoring checkpoint ***************')

if __name__ == "__main__":
    device_config_dict = dict(
        cisco3='cisco3.lasthop.io-loopbacks',
        arista1='arista1.lasthop.io-loopbacks',
    )
    connection_object_list = []
    for k, v in device_dict.items():
        this_conn_obj = open_napalm_connection(**v)
        connection_object_list.append(this_conn_obj)
#####        do_napalm_getter(this_conn_obj, 'get_arp_table')
####        do_napalm_getter(this_conn_obj, 'get_ntp_peers')
###        create_backup(this_conn_obj)
##        print(k, 'config load')
##        config_merge_napalm(this_conn_obj, device_config_dict[k])
#        create_checkpoint(this_conn_obj)
        if k == 'nxos1':
            restore_checkpoint(this_conn_obj, 'nxos1-checkpoint-2022-02-06T10')

