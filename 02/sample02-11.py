import xml.etree.ElementTree as ET

root = ET.Element('animal')
human = ET.SubElement(root, 'human')
# 頭の体操
# persons = list(map(lambda i: ET.SubElement(human, 'person', attrib={'id': str(i)}), range(10)))
persons = []
for i in range(10):
    person = ET.SubElement(human, 'person')
    person.attrib['id'] = str(i) # cast i from int to str
    persons.append(person)

# write readable xml (have your attention to 'wb')
with open('./02/animal.xml', 'wb') as f:
    import xml.dom.minidom as md
    f.write(md.parseString(ET.tostring(root, encoding='utf-8', xml_declaration=True)).toprettyxml(indent='  ',encoding="utf-8"))


# write xml wituout indent
# ET.ElementTree(new_routes).write('sorted_rou.xml', encoding='UTF-8')

# convet to json
# xmltodict module is required. Run `pip install xmldict`
# import xmltodict
# json_data = json.dumps(xmltodict.parse(ET.tostring(root)))
# print(json_data)
# '{"animal": {"human": {"person": [{"@id": "0"}, {"@id": "1"}, {"@id": "2"}, {"@id": "3"}, {"@id": "4"}, {"@id": "5"}, {"@id": "6"}, {"@id": "7"}, {"@id": "8"}, {"@id": "9"}]}}}'