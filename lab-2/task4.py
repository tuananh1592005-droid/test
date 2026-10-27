
import xml.etree.ElementTree as ET

# Read the XML file
root = ET.parse("currency.xml").getroot()

# Create two empty lists
names = []
values = []

# Get currency names and values
for currency in root.findall("Valute"):
    name = currency.findtext("Name")
    value = currency.findtext("Value")

    names.append(name)
    values.append(float(value.replace(",", ".")))

# Print the results
print("========== ЗАДАНИЕ 4 ==========")
print("Name:", names)
print("Value:", values)
