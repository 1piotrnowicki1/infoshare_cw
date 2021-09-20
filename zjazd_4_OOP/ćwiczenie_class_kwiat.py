"""
Klasa Kwiat:
atrybuty instancji:
nazwa,kolor, odmiana, wzrost
funkcjonalnosc: rosnij, malej

"""


class Kwiat:

    def __init__(self, name, kolor, odmiana, wzrost ):
        self.name = name
        self.kolor = kolor
        self.odmiana = odmiana
        self.wzrost = wzrost

    def rosnij(self):
        self.wzrost += 1

    def malej(self):
        self.wzrost -= 1

print('Sadzimy kwiat')
kwiat = Kwiat('roza', 'red', 'k1', 30)
for i in range(15):
    print(f'W dniu {i} wysokość kwiata wynosi: {kwiat.wzrost}')
    kwiat.rosnij()
    
