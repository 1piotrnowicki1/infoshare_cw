"""
Klasa Pies:
atrybuty instancji:
imie, rasa, wzrost, waga
funkcje:
poglaszcz, szczekaj

"""

class Pies:

    def __init__(self, imie, rasa, wzrost, waga):
        self.imie = imie
        self.rasa = rasa
        self.wzrost = wzrost
        self.waga = waga

    def poglaszcz(self):
        print('Głaskanie pasa')

    def szczekaj(self):
        print('HOw HOW')


pies = Pies('Reksio', 'kundel', 30, 20)

pies.poglaszcz()

