"""

Napisz funkcję która:
 - symuluje rzut kostką do gry (6 stronna)

Napisz funkcję która:
 - symuluje określoną ilość rzutów kością i zwraca True gdy pewna liczba wypadła conajmniej 2 razy

Napisz funkcję która:
 - symuluje określoną ilość razy rzut dwoma koścmi jednocześnie, a następnie zwraca proporcje ile
   razy w ciągu tych rzutów na obu kościach wypadły te same numery

"""

import random

def rzut_kostka():
    kostka = [1, 2, 3, 4, 5, 6]
    return random.choice(kostka)


def rzut_kostka_check_duplicate():
    n = int(input("Podaj liczbę rzutów: "))
    nowe_rzuty = []
    for idx in range(n):
        wynik = rzut_kostka()
        nowe_rzuty.append(wynik)
    print(nowe_rzuty)

    if len(nowe_rzuty) == len(set(nowe_rzuty)):
        return False
    else:
        return True


rzut_kostka()
print(rzut_kostka_check_duplicate())
