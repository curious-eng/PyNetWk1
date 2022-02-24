#!usr/bin/env python

from pprint import pprint
import requests
from urllib3.exceptions import InsecureRequestWarning
import os
import json

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == "__main__":
    token = os.environ["NETBOX_TOKEN"]

    url = 'https://netbox.lasthop.io/api/ipam/ip-addresses/'
    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    post_data = {"address": "192.0.2.211/32"}
        
    response = requests.post(url, headers=http_headers, data=json.dumps(post_data), verify=False)
    response = response.json()

#display the new object
    my_new_id = response['id']
    print('New id: ', my_new_id)
    url = 'https://netbox.lasthop.io/api/ipam/ip-addresses/' + str(my_new_id) + '/'
    http_get_headers = {"Content-Type": "application/json; version=2.4;"}
    if token:
        http_get_headers['Authorization'] = 'Token {}'.format(token)

    response = requests.get(url, headers=http_get_headers,  verify=False)
    response = response.json()
    print('Display new object')
    pprint(response)

#add description
    print('Add description')
    post_data['description'] = 'IP address to be deleted'
    response = requests.put(url, headers=http_headers, data=json.dumps(post_data), verify=False)
    response = response.json()
    pprint(response)

#delete new record
    http_del_headers = {}
    http_del_headers["Content-Type"] = "application/json; version=2.4;"
    http_del_headers["Authorization"] = f"Token {token}"
    response = requests.delete(url, headers=http_del_headers, verify=False)
    #response = response.json()
    print('Delete')
    pprint(response)
