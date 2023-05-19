import sys


def parse_arguments():
    if len(sys.argv) != 1:
        print("Użyj: program.exe")
        sys.exit(1)

    pathFile1 = input("Podaj ścieżkę pliku wejściowego: ")
    pathFile2 = input("Podaj ścieżkę pliku wyjściowego: ")

    # Sprawdź rozszerzenia plików
    ext1 = pathFile1.split(".")[-1]
    ext2 = pathFile2.split(".")[-1]

    if ext1 not in ['xml', 'json', 'yml']:
        print("Nieobsługiwane rozszerzenie pliku: {}".format(ext1))
        sys.exit(1)

    if ext2 not in ['xml', 'json', 'yml']:
        print("Nieobsługiwane rozszerzenie pliku: {}".format(ext2))
        sys.exit(1)

    return pathFile1, pathFile2


if __name__ == "__main__":
    pathFile1, pathFile2 = parse_arguments()
    print("Ścieżka pliku wejściowego: {}".format(pathFile1))
    print("Ścieżka pliku wyjściowego: {}".format(pathFile2))

    # Tutaj możesz dodać dalsze operacje związane z Taskiem 1
