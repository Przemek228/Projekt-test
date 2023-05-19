import tkinter as tk
from tkinter import filedialog
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

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Pliki XML", "*.xml")])
    if file_path:
        root = parse_xml_file(file_path)
        if root is not None:
            text.insert(tk.END, "Załadowano plik: {}\n".format(file_path))
            for element in root:
                if element.tag == "adres":
                    text.insert(tk.END, "{}:\n".format(element.tag))
                    for subelement in element:
                        text.insert(tk.END, "  {}: {}\n".format(subelement.tag, subelement.text))
                elif element.tag == "zainteresowania":
                    text.insert(tk.END, "{}:\n".format(element.tag))
                    for subelement in element:
                        text.insert(tk.END, "  {}\n".format(subelement.text))
                else:
                    text.insert(tk.END, "{}: {}\n".format(element.tag, element.text))
            text.insert(tk.END, "\n")
    else:
        text.insert(tk.END, "Nie wybrano pliku.\n\n")

def save_file():
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

    file_path = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("Pliki XML", "*.xml")])
    if file_path:
        tree = convert_to_xml(data)
        save_xml_file(tree, file_path)
        text.insert(tk.END, "Zapisano dane do pliku: {}\n\n".format(file_path))
    else:
        text.insert(tk.END, "Nie wybrano ścieżki do zapisu pliku.\n\n")

def clear_text():
    text.delete(1.0, tk.END)

# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.title("Program do konwersji danych")
root.geometry("400x300")

# Tworzenie przycisków
open_button = tk.Button(root, text="Otwórz plik", command=open_file)
open_button.pack(pady=10)

save_button = tk.Button(root, text="Zapisz dane", command=save_file)
save_button.pack(pady=10)

clear_button = tk.Button(root, text="Wyczyść", command=clear_text)
clear_button.pack(pady=10)

# Tworzenie pola tekstowego
text = tk.Text(root, height=15, width=50)
text.pack()

root.mainloop()
