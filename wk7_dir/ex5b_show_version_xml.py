from lxml import etree
import xmltodict
#import xml.etree.ElementTree as etree

def read_file(filename, mode = "r"):    #defaults to 'read' mode but allows you to specify mode (presumably could also 'w')
    with open(filename, mode) as f:
        data = f.read()
    return(data)
#    return(etree.parse(filename, mode).getroot())

my_xml = read_file("show_version.xml", "rb")
my_root = etree.fromstring(my_xml).getroottree()#.getroot()
my_search = my_root.find(".//{*}proc_board_id")
#print(my_search, my_search.tag, my_search.text)
print(my_search)
#print(my_root.tag)
#for k, v in my_root.nsmap.items():
#    print("namespace ID: {} namespace: {}".format(k, v))
#sszt = read_file("show_security_zones_trust.xml")

