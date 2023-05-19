import json

def write_json_file(data, file_path):
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        print("Dane zostały zapisane do pliku: {}".format(file_path))
    except Exception as e:
        print("Błąd podczas zapisywania danych do pliku: {}".format(file_path))
        print(e)

def task3(data):
    file_path = input("Podaj ścieżkę do pliku .json, w którym chcesz zapisać dane: ")
    write_json_file(data, file_path)

if __name__ == "__main__":
    data_from_task2 = {
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
    task3(data_from_task2)
