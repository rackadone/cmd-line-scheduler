import xml.etree.ElementTree as ET

tree = ET.parse('sample.xml')
root = tree.getroot()
print root.tag
print root.attrib

#Ctrl+Shift+/ << block comment in subl

# for child in root:
#     print child.tag, child.attrib
# print root[0][1].text # Prints 2008

for neighbor in root.iter('neighbor'):
    print neighbor.attrib

# Prints the following:
# {'direction': 'E', 'name': 'Austria'}
# {'direction': 'W', 'name': 'Switzerland'}
# {'direction': 'N', 'name': 'Malaysia'}
# {'direction': 'W', 'name': 'Costa Rica'}
# {'direction': 'E', 'name': 'Colombia'}

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print rank, name