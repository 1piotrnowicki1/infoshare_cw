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
    ("Karol", "Kowalski")
]

def wyszukiwarka():
    for osoba in baza_1:
        if osoba[0] == "Marek":
            print("Cześć Marek")
        else:
            print("To nie Marek")
        print(osoba)

if __name__ == "__main__":
    wyszukiwarka()