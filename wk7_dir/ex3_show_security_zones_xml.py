from lxml import etree
import xmltodict
#import xml.etree.ElementTree as etree

def read_file(filename):
    #with open(filename) as file:
    #    xml_string = file.read()
    #my_dict = xmltodict.parse(xml_string)
    return(etree.parse(filename).getroot())

#my_files=["show_security_zones.xml", "show_security_zones_trust.xml"]
#xml_list = []
#for a in my_files:
#    xml_list.append(read_file(a))
# xml_list[0].getroot().getchildren()

ssz = read_file("show_security_zones.xml")
sszt = read_file("show_security_zones_trust.xml")
#ssz.getroot().getchildren()[0].getchildren()

