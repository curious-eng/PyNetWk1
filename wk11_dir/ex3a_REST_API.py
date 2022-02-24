#!usr/bin/env python

from pprint import pprint
import requests
from urllib3.exceptions import InsecureRequestWarning
import os

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == "__main__":
    token = os.environ["NETBOX_TOKEN"]

    url = 'https://netbox.lasthop.io/api/dcim/devices/'
    http_headers = {"accept": "application/json; version=2.4;"}
    if token:
        http_headers['Authorization'] = 'Token {}'.format(token)

    response = requests.get(url, headers=http_headers, verify=False)
    response = response.json()
    for item in response['results']:
        print(40 * '-')
        print(item['display_name'])
        print(10 * '-')
        print('Location:',item['site']['name'])
        print('Vendor:',item['device_type']['manufacturer']['name'])
        print('Status:',item['status']['label'])
        print(40 * '-')
        print('\n')

