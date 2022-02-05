from getpass import getpass
srx2 = {
    "host": "srx2.lasthop.io",
    "user": "pyclass",
    "password": getpass(),
    "device_params": {"name": "junos"},
    "hostkey_verify": False,
    "look_for_keys": False,
    "allow_agent": False,
    "port": 830,
    "timeout": 60,
}
#srx2 = (
#    host="srx2.lasthop.io",
#    username="pyclass",
#    password=getpass(),
#    device_params={"name": "junos"},
#    hostkey_verify=False,
#    look_for_keys=False,
#    allow_agent=False,
#    port=830,
#    timeout=60,
#)

