class Kwiat:
    def __init__(self, nazwa=None, kolor=None, kolor_doniczki=None):
        self.nazwa = nazwa
        self.kolor = kolor
        self.kolor_doniczki = kolor_doniczki

    def podlewanie(self):
        print('kwiat jest podlewany...')

    def zmiana_doniczki(self):
        print('zmieniamy kolor doniczki')
        self.kolor_doniczki = input('Podaj kolor nowej doniczki: ')

kwiat1 = Kwiat("paprotka", "zielony", "żółty")
print(vars(kwiat1))
kwiat1.podlewanie()
kwiat1.zmiana_doniczki()
print(vars(kwiat1))