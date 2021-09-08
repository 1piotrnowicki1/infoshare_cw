"""
1. stworzyć zmienną baza1 z 5 osobami gdzie kazda osoba to tupla z imieniem i nazwiskiem. Baza jest listą tych tupli
2. baza2 będzie słownikiem, gdzie kluczem będą tuple z imieniem i nazwiskiem a wartością nr telefonu
3. stworzyć funkcję która za pomocą for loop będzie w baza1 szukać osoby imieniem Andrzej - wtedy kończymy program.
   Jeżeli imie tej osogy to Marek to wyprintujemy "Cześć Marek"
4. stworzyć funkcję która za pomocą pętli while będzie szukać Karoliny Nowak - jeśli ją znajdziemy to chcemy wyświetlić jej nr tel
5. dodać typowanie do funkcji

6. funkcje uruchamiamy w bloku if __ name __ == '__ main __':

"""

baza_1 = [
    ("Basia", "Mig"),
    ("Ala", "Kot"),
    ("Ewa", "Sat"),
    ("Marek", "Nowak"),
    ("Adam", "Bak"),
    ("Karol", "Kowalski")
]

baza_2 = {
    ("Basia", "Mig"): "23434",
    ("Ala", "Kot"): "23437",
    ("Ewa", "Sat"): "04564",
    ("Marek", "Nowak"): "0456056",
    ("Adam", "Bak"): "054534",
    ("Karol", "Kowalski"): "014325"
}

def wyszukiwarka():
    for idx, osoba in enumerate(baza_1):
        print(idx)
        if osoba[0] == "Marek":
            print("Cześć Marek")
        elif osoba[0] == "Ewa":
            pass
        else:
            print("To nie Marek")
        print(str(osoba) + "\n")
    print("Koniec for loopa")


def wyszukiwarka_nazwiska(imie):
    count = 0
    nazwisko = None
    while not nazwisko:
        if baza_1[count][0] == imie:
            nazwisko = baza_1[count][1]
        count += 1
    print(nazwisko)


if __name__ == "__main__":
    # wyszukiwarka()

    for idx in range(3,10,2):
        print(idx)

    wyszukiwarka_nazwiska("Ewa")




