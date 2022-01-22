from lxml import etree
import xmltodict
#import xml.etree.ElementTree as etree

def read_file(filename, jb_force_list = {}):#"zones-security": True}):#optional force list
    with open(filename) as file:
        xml_string = file.read()
    return(xmltodict.parse(xml_string, force_list = jb_force_list))

jb_force_list = {"zones-security": True}
ssz = read_file("show_security_zones.xml", jb_force_list)
sszt = read_file("show_security_zones_trust.xml", jb_force_list)
print()
print("show security zones.xml       ['zones-information']['zones-security'] is type:   {}".format(type(ssz['zones-information']['zones-security'])))
print("show security zones trust.xml ['zones-information']['zones-security'] is type:   {}".format(type(sszt['zones-information']['zones-security']))    )

