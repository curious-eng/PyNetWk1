#!/usr/bin/env python

from pprint import pprint
import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == "__main__":
    url = 'https://netbox.lasthop.io/api/'
    http_headers = {"accept": "application/json; version=2.4;"}
    response = requests.get(url, headers=http_headers, verify=False)

    print('\n', 'status code:')
    response1 = response.status_code
    pprint(response1)
    print('\n','text:')
    response2 = response.text
    pprint(response2)
    print('\n', 'response headers:')
    response3 = response.headers
    pprint(dict(response3))
    print('\n', 'json:')
    response4 = response.json()
    pprint(response4)
    print()

