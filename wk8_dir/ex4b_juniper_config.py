
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass

a_device = Device(host='srx2.lasthop.io', user='pyclass', password=getpass())
a_device.open()
a_device.timeout = 60

cfg = Config(a_device)
cfg.lock()

cfg.load(path='static_routes.conf', format='text', merge=True)
cfg.commit()

