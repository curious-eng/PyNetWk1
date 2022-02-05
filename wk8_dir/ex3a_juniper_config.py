
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass
from jnpr_devices import srx2

a_device = Device(**srx2)
a_device.open()
a_device.timeout = 60

cfg = Config(a_device)
cfg.lock()
#a = cfg.lock()
try:
    cfg.lock()
except: # LockError:
    print("an error occurred")#LockError")
cfg.unlock()

