#!usr/bin/env python

from pprint import pprint
import requests
from urllib3.exceptions import InsecureRequestWarning
import os
import json

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def my_api_get(url, http_headers):
    return(requests.get(url, headers=http_headers, verify=False))

if __name__ == "__main__":
    token = os.environ["NETBOX_TOKEN"]

    url = 'https://netbox.lasthop.io/api/ipam/ip-addresses/'
    http_headers = {"Content-Type": "application/json; version=2.4;"}
    post_data = {"address": "192.0.2.199/32"}
    if token:
        http_headers['Authorization'] = 'Token {}'.format(token)
       
    response = my_api_get(url, http_headers)
#    response = requests.post(url, headers=http_headers, data=json.dumps(post_data), verify=False)
    response = response.json()
#    my_count = 0
    my_loop_continue = True
    while my_loop_continue: #not response['next'] is None:
        for item in response['results']:
            print(item['id'], item['address'], item['description'])
            #pprint(item['id'])
        if not response['next'] is None:
            url = response['next']
            response = my_api_get(url, http_headers)
            response = response.json()
        else:
            my_loop_continue = False
#
#    pprint(response)
#{'count': 220,
# 'next': 'http://netbox.lasthop.io/api/ipam/ip-addresses/?limit=50&offset=50',
# 'previous': None,
# 'results': [{'id': 289,
#    print(response['next'])
#    url = response['next']
#    response = my_api_get(url, http_headers)
#    response = response.json()
#    print(response['next'])
#    url = response['next']
#    response = my_api_get(url, http_headers)
#    response = response.json()
#    print(response['next'])
#    url = response['next']
#    response = my_api_get(url, http_headers)
#    response = response.json()
#    print(response['next'])
#    url = response['next']
#    response = my_api_get(url, http_headers)
#    response = response.json()
#    print(response['next'])

