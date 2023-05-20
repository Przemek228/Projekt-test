import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
import concurrent.futures

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
        elif key == "zainteresowania":
            element = ET.SubElement(root, key)
            for subvalue in value:
                subelement = ET.SubElement(element, "zainteresowanie")
                subelement.text = str(subvalue)
        else:
            element = ET.SubElement(root, key)
            element.text = str(value)

    tree = ET.ElementTree(root)
    return tree

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Pliki XML", "*.xml")])
    if file_path:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(parse_xml_file, file_path)
            root = future.result()

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
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(convert_to_xml, data)
            tree = future.result()

        if tree is not None:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(save_xml_file, tree, file_path)
                future.result()
    else:
        text.insert(tk.END, "Nie wybrano ścieżki do zapisu pliku.\n\n")

def clear_text():
    text.delete(1.0, tk.END)

# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.title("Program do konwersji danych")
root.geometry("400x300")

# Ustawienie tła
root.configure(bg="#F0F0F0")

# Tworzenie przycisków
open_button = tk.Button(root, text="Otwórz plik", command=open_file, font=("Comic Sans MS", 14, "bold"),
                        bg="#246100", fg="white")
open_button.pack(pady=10)

save_button = tk.Button(root, text="Zapisz dane", command=save_file, font=("Comic Sans MS", 14, "bold"),
                        bg="#046494", fg="white")
save_button.pack(pady=10)

clear_button = tk.Button(root, text="Wyczyść", command=clear_text, font=("Comic Sans MS", 14, "bold"),
                         bg="#8f0601", fg="white")
clear_button.pack(pady=10)

# Tworzenie pola tekstowego
text = tk.Text(root, height=15, width=50)
text.pack()

root.mainloop()
