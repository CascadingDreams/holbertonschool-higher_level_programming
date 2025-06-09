#!/usr/bin/python3

"""XML serialization module"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize dictionary to XML file"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize XML file to dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        key = child.tag
        value = child.text
        result[key] = value
    return result
