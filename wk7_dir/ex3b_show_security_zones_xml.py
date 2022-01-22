from lxml import etree
import xmltodict
#import xml.etree.ElementTree as etree

def read_file(filename):
    with open(filename) as file:
        xml_string = file.read()
    return(xmltodict.parse(xml_string))
    #return(etree.parse(filename).getroot())

#my_files=["show_security_zones.xml", "show_security_zones_trust.xml"]
#xml_list = []
#for a in my_files:
#    xml_list.append(read_file(a))
# xml_list[0].getroot().getchildren()

ssz = read_file("show_security_zones.xml")
sszt = read_file("show_security_zones_trust.xml")
#ssz.getroot().getchildren()[0].getchildren()
print()
print("show security zones.xml       ['zones-information']['zones-security'] is type:   {}".format(type(ssz['zones-information']['zones-security'])))
print("show security zones trust.xml ['zones-information']['zones-security'] is type:   {}".format(type(sszt['zones-information']['zones-security']))    )
