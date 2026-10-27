import csv
import xml.etree.ElementTree as ET


# Read books from a CSV file
def read_books(filename):
    with open(filename, encoding="latin-1", newline="") as file:
        return list(csv.DictReader(file, delimiter=";"))


# Read currency names and values from an XML file
def read_currencies(filename):
    root = ET.parse(filename).getroot()
    names = []
    values = []

    for currency in root.findall("Valute"):
        names.append(currency.findtext("Name"))
        value = currency.findtext("Value").replace(",", ".")
        values.append(float(value))

    return names, values


# Save text to a file
def write_file(filename, text):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
