
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass

a_device = Device(host='srx2.lasthop.io', user='pyclass', password=getpass())
a_device.open()
a_device.timeout = 60

cfg = Config(a_device)
cfg.lock()

cfg.load("delete routing-options static route 203.0.113.5/32", format="set", merge=True)
cfg.load("delete routing-options static route 203.0.113.200/32", format="set", merge=True)
cfg.commit()

