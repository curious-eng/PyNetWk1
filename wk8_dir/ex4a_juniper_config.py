from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass
from jnpr_devices import srx2
from jnpr.junos.op.routes import RouteTable

a_device = Device(**srx2)
a_device.open()
a_device.timeout = 60

#cfg = Config(a_device)
#cfg.lock()
#my_lockerror = False
#try:
#    cfg.lock()
#except: # LockError:
#    print("an error occurred")#LockError")
#    my_lockerror = True
#if not my_lockerror:
#    cfg.load("set system host-name jb123", format="set", merge=True)
#    cfg.load("set system host-name srx2", format="set", merge=True)
#    print(cfg.diff())
#    cfg.rollback(0)
#    print(cfg.diff())
#cfg.unlock() - fails dueto close/open to get new hostname
my_routes = RouteTable(a_device)#, path='inet.0')#, table='inet.0')
my_routes.get()
#pprint(my_routes)
for k,v in my_routes.items():
    print('{} type: {}, interface: {}, next-hop: {}'.format(k, v[0][1], v[1][1], v[3][1]))

