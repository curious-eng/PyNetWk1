from pprint import pprint
from lxml import etree
import xmltodict
#import xml.etree.ElementTree as etree
#my_xml = etree.parse("show_security_zones.xml")
xml_string = '''
<zones-information>
    <zones-security>
        <zones-security-zonename>trust</zones-security-zonename>
        <zones-security-send-reset>Off</zones-security-send-reset>
        <zones-security-policy-configurable>Yes</zones-security-policy-configurable>
        <zones-security-interfaces-bound>1</zones-security-interfaces-bound>
        <zones-security-interfaces>
            <zones-security-interface-name>vlan.0</zones-security-interface-name>
        </zones-security-interfaces>
    </zones-security>
    <zones-security>
        <zones-security-zonename>untrust</zones-security-zonename>
        <zones-security-send-reset>Off</zones-security-send-reset>
        <zones-security-policy-configurable>Yes</zones-security-policy-configurable>
        <zones-security-screen>untrust-screen</zones-security-screen>
        <zones-security-interfaces-bound>2</zones-security-interfaces-bound>
        <zones-security-interfaces>
            <zones-security-interface-name>fe-0/0/0.0</zones-security-interface-name>
            <zones-security-interface-name>pt-1/0/0.0</zones-security-interface-name>
        </zones-security-interfaces>
    </zones-security>
    <zones-security>
        <zones-security-zonename>junos-host</zones-security-zonename>
        <zones-security-send-reset>Off</zones-security-send-reset>
        <zones-security-policy-configurable>Yes</zones-security-policy-configurable>
        <zones-security-interfaces-bound>0</zones-security-interfaces-bound>
        <zones-security-interfaces>
        </zones-security-interfaces>
    </zones-security>
</zones-information>
'''
my_dict = xmltodict.parse(xml_string)
#pprint(my_dict)
for counter, list_item in enumerate(my_dict['zones-information']['zones-security']):      #this is a 3 item list, containing odicts
    #print(counter, list_item)
    print("security zone#:{} {}".format(counter +1, list_item['zones-security-zonename']))
