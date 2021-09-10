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
    nowe_rzuty = []
    for idx in range(throws):
        wynik = rzut_kostka()
        nowe_rzuty.append(wynik)
    print(nowe_rzuty)

    if len(nowe_rzuty) == len(set(nowe_rzuty)):
        return False
    else:
        return True


def double_dice_throw():
    number_of_doubles = 0
    for idx in range(throws):
        result1 = rzut_kostka()
        result2 = rzut_kostka()
        print(f'Result 1: {result1} Result 2: {result2}')
        if result1 == result2:
            number_of_doubles += 1
    return number_of_doubles


throws = int(input("Podaj liczbę rzutów: "))

rzut_kostka()
print(rzut_kostka_check_duplicate())
print(f'Przy rzucie dwoma kośćmi było {double_dice_throw()} powtórzeń')
