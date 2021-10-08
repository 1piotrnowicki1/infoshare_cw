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


kwiat = Kwiat('roza', 'red', 'k1', 30)
print(f'Sadzimy kwiat {kwiat.name}')
for i in range(15):
    print(f'W dniu {i} wysokość kwiata wynosi: {kwiat.wzrost}')
    kwiat.rosnij()
    
