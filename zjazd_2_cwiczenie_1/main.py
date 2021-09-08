from typing import Tuple

def funkcja(imie:str, nazwisko:str) -> Tuple[str, str]:
    print(type(imie), type(nazwisko))
    return imie, nazwisko


if __name__ == "__main__":
    imie, nazwisko = funkcja(1, 2)
    print(imie, nazwisko)
    print(type(imie))
