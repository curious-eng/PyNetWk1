from lxml import etree
import xmltodict
#import xml.etree.ElementTree as etree

def read_file(filename):
    return(etree.parse(filename).getroot())

ssz = read_file("show_security_zones.xml")
sszt = read_file("show_security_zones_trust.xml")

my_root = ssz.find(".//zones-security")
print("Find tag of the first zones-security element")
print("-" * 20)
print(my_root.tag)
print()
print("Find tag of all child elements of the first zones-security element")
print("-" * 20)
for my_child in my_root.getchildren():
    print(my_child.tag)
#ssz.find(".//zones-security").tag
#Out[3]: 'zones-security'

#In [4]: ssz.find(".//zones-security").getchildren()

