import yaml

def write_yaml_file(data, file_path):
    try:
        with open(file_path, "w") as file:
            yaml.dump(data, file)
        print("Dane zapisane do pliku {}".format(file_path))
    except IOError:
        print("Błąd podczas zapisu do pliku {}".format(file_path))

def task5():
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

    file_path = input("Podaj ścieżkę do pliku .yml, w którym chcesz zapisać dane: ")
    write_yaml_file(data, file_path)

if __name__ == "__main__":
    task5()
