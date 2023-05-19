import yaml

def read_yaml_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
        return data
    except FileNotFoundError:
        print("Plik {} nie istnieje.".format(file_path))
    except yaml.YAMLError as e:
        print("Błąd w składni pliku YAML: {}".format(file_path))
        print(e)

def task4():
    file_path = input("Podaj ścieżkę do pliku .yml: ")
    data = read_yaml_file(file_path)
    if data is not None:
        print("Wczytane dane:")
        print(data)

if __name__ == "__main__":
    task4()
