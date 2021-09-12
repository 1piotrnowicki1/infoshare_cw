"""
Napisać program bankomat który:
 - W słowniku karty przechowa informacje pod postacią ‘numer konta’ : {‘pin’: 1234, ‘saldo’: 1234}
 - Poprosi użytkownika o numer konta, a następnie gdy dany numer konta istnieje poprosi o numer pin.
 - Pozwoli użytkownikowi na dane opcje: odczytaj saldo, wpłać pieniądze, wypłać pieniądze, zmień kod PIN
 - Wyzwanie: zastanów się i zaimplementuj, w jaki sposób można przechowywać historię operacji. Zaimplementuj swoje rozwiązanie.

"""

karty = {'0000' : {'pin': 1234, 'saldo': 10000}}
nr_konta = input('Podaj numer karty: ')

def authenticate_user():
    if numer_konta in karty:
        pin = int(input("Podaj pin: "))
        if karty[nr_konta]['pin']
