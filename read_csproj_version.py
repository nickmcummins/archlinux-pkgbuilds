import xml.etree.ElementTree as ET
import sys

csprojfile = sys.argv[1]

version = ET.parse(csprojfile).getroot().findall('.//Version')[0]
print(version.text)