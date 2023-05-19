import json

def read_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Plik {} nie istnieje.".format(file_path))
    except json.JSONDecodeError:
        print("Błąd w składni pliku JSON: {}".format(file_path))

def task2():
    while True:
        file_path = input("Podaj ścieżkę do pliku JSON: ")
        data = read_json_file(file_path)
        if data is not None:
            # Tutaj możesz dodać dalsze operacje na wczytanych danych
            print("Dane z pliku {}: {}".format(file_path, data))
            break

if __name__ == "__main__":
    task2()
