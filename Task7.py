import xml.etree.ElementTree as ET

def convert_to_xml(data):
    root = ET.Element("root")

    for key, value in data.items():
        if isinstance(value, dict):
            element = ET.SubElement(root, key)
            for subkey, subvalue in value.items():
                subelement = ET.SubElement(element, subkey)
                subelement.text = str(subvalue)
        else:
            element = ET.SubElement(root, key)
            element.text = str(value)

    tree = ET.ElementTree(root)
    return tree

def save_xml_file(tree, file_path):
    try:
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
        print("Dane zostały zapisane do pliku XML: {}".format(file_path))
    except IOError:
        print("Błąd: Nie można zapisać danych do pliku XML: {}".format(file_path))

def task7():
    data = {
        "imie": "Gumball",
        "nazwisko": "Waterson",
        "wiek": 20,
        "adres": {
            "ulica": "York Street",
            "miasto": "Vallejo",
            "kod_pocztowy": "CA 94590"
        },
        "zainteresowania": ["programowanie", "sport", "gotowanie"]
    }

    file_path = input("Podaj ścieżkę do pliku .xml, do którego chcesz zapisać dane: ")
    tree = convert_to_xml(data)
    save_xml_file(tree, file_path)

if __name__ == "__main__":
    task7()
