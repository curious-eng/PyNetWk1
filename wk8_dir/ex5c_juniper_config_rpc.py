#!/usr/bin/env python

from jnpr.junos import Device
from lxml import etree
from getpass import getpass
from pprint import pprint

srx_cred_dict = {'host': 'srx2.lasthop.io', 'user': 'pyclass', 'password': getpass()}

a_device = Device(**srx_cred_dict)
a_device.open()

xml_out = a_device.rpc.get_interface_information(interface_name="fe-0/0/7", terse=True, normalize=True)
my_xml_string = etree.tostring(xml_out, encoding='unicode', pretty_print=True)
print(my_xml_string)
#pyclass@srx2> show interfaces terse | display xml rpc
#<rpc-reply xmlns:junos="http://xml.juniper.net/junos/12.1X46/junos">
#    <rpc>
#        <get-interface-information>
#                <terse/>
#        </get-interface-information>
#    </rpc>
#    <cli>
#        <banner></banner>
#    </cli>
#</rpc-reply>
#
#pyclass@srx2>
#
#    tostring(element_or_tree, encoding=None, method="xml",
#                 xml_declaration=None, pretty_print=False, with_tail=True,
#                 standalone=None, doctype=None,
#                 exclusive=False, inclusive_ns_prefixes=None,
#                 with_comments=True, strip_text=False,
#                 )

