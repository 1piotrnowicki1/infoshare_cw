"""
klasa Czlowiek:
atrybuty instancji:
imie, nazwisko, wiek
funkcje:
podaj_imie, zmien_imie, przedstaw_sie, podaj_wiek, zmien_wiek, podaj_nazwisko, zmien_nazwisko

"""

class Czlowiek:
    def __init__(self, imie=None, nazwisko=None, wiek=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def podaj_imie(self):
        self.imie = input('Podaj imie: ')
        self.nazwisko = input('Podaj nazwisko: ')
        self.wiek = input('Podaj wiek: ')

    def zmien_imie(self):
        self.imie = input('Podaj nowe imie: ')
        self.nazwisko = input('Podaj nowe nazwisko: ')
        self.wiek = input('Podaj nowe wiek: ')

    def przedstaw_sie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lata')

czlowiek = Czlowiek()
czlowiek.podaj_imie()
print(czlowiek.imie)
print(czlowiek.nazwisko)
print(czlowiek.wiek)

czlowiek.zmien_imie()
czlowiek.przedstaw_sie()

print(vars(czlowiek))