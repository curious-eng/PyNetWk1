
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass
from jnpr_devices import srx2


a_device = Device(**srx2)
a_device.open()
a_device.timeout = 60

cfg = Config(a_device)
#cfg.lock()
my_lockerror = False
try:
    cfg.lock()
except: # LockError:
    print("an error occurred")#LockError")
    my_lockerror = True
if not my_lockerror:
#    print("hostname before config:", a_device.facts['hostname'])
    cfg.load("set system host-name jb123", format="set", merge=True)
#    cfg.load("set system host-name srx2", format="set", merge=True)
#    cfg.commit()
#    a_device.close()
#    a_device.open()
#    print("hostname after config:", a_device.facts['hostname'])
    print(cfg.diff())
    cfg.rollback(0)
    print(cfg.diff())
#cfg.unlock() - fails dueto close/open to get new hostname

