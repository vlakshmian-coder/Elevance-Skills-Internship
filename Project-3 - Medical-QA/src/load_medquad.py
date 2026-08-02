import os
import xml.etree.ElementTree as ET

xml_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "MedQuAD-master",
    "1_CancerGov_QA",
    "0000001_1.xml"
)

print("Reading:")
print(xml_path)

tree = ET.parse(xml_path)
root = tree.getroot()

print("\nRoot:", root.tag)

print("\nChildren:")

for child in root:
    print(child.tag)