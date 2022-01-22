from lxml import etree
import xmltodict
#import xml.etree.ElementTree as etree

def read_file(filename, mode = "r"):    #defaults to 'read' mode but allows you to specify mode (presumably could also 'w')
    with open(filename, mode) as f:
        data = f.read()
    return(data)
#    return(etree.parse(filename, mode).getroot())

my_xml = read_file("show_version.xml", "rb")
my_root = etree.fromstring(my_xml).getroottree().getroot()
#print(my_root.tag)
for k, v in my_root.nsmap.items():
    print("namespace ID: {} namespace: {}".format(k, v))
#sszt = read_file("show_security_zones_trust.xml")

#my_root = ssz.find(".//zones-security")
#print("Find tag of the first zones-security element")
#print("-" * 20)
#print(my_root.tag)
#print()
#print("Find tag of all child elements of the first zones-security element")
#p##rint("-" * 20)
#for my_child in my_root.getchildren():
#    print(my_child.tag)
#ssz.find(".//zones-security").tag
#Out[3]: 'zones-security'

#In [4]: ssz.find(".//zones-security").getchildren()

