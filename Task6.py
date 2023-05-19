import xml.etree.ElementTree as ET

def parse_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        print("Poprawna składnia pliku XML: {}".format(file_path))
        return root
    except ET.ParseError:
        print("Błąd: Nieprawidłowa składnia pliku XML: {}".format(file_path))
        return None
    except IOError:
        print("Błąd: Nie można odczytać pliku XML: {}".format(file_path))
        return None

def task6():
    file_path = input("Podaj ścieżkę do pliku .xml, który chcesz wczytać: ")
    root = parse_xml_file(file_path)

    # Przykład wykorzystania wczytanych danych
    if root is not None:
        for element in root:
            if element.tag == "adres":
                print("{}:".format(element.tag))
                for subelement in element:
                    print("  {}: {}".format(subelement.tag, subelement.text))
            elif element.tag == "zainteresowania":
                print("{}:".format(element.tag))
                for subelement in element:
                    print("  {}: {}".format(subelement.tag, subelement.text))
            else:
                print("{}: {}".format(element.tag, element.text))

if __name__ == "__main__":
    task6()
