from lxml import etree
import xmltodict
#import xml.etree.ElementTree as etree

def read_file(filename):
    return(etree.parse(filename).getroot())

ssz = read_file("show_security_zones.xml")
sszt = read_file("show_security_zones_trust.xml")

my_element = ssz.findall(".//zones-security")
for element in my_element:
    print(element.tag, element.find(".//zones-security-zonename").text)

