"""
Napisz funkcję która:
 - Symuluje rzut monetą
 - Rzuca monetą określoną ilość razy i zwraca najdłuższy ciąg orlów

Zeby bylo prosciej, mozecie przyjac ze wartosc Reszki to 0, a orła 1

"""

import random


def rzut_moneta():
    return random.choice([0, 1])


def rzut_moneta_n_razy(n):
    current_streak, longest_streak, poprzedni_rzut = 0, 0, 0
    for i in range(n):
        wynik_rzutu = rzut_moneta()
        print(f'Poprzedni rzut: {poprzedni_rzut}')
        print(f'Wynik rzutu: {wynik_rzutu}')
        print(f'Current streak: {current_streak}')
        print(f'Longest streak: {longest_streak}')
        print(10 * '*')
        if wynik_rzutu == 1 and poprzedni_rzut == 1:
            poprzedni_rzut = 1
            current_streak += 1
            longest_streak = max(current_streak, longest_streak)
        elif wynik_rzutu == 1:
            poprzedni_rzut = 1
            current_streak += 1
        else:
            longest_streak = max(current_streak, longest_streak)
            current_streak = 0
            poprzedni_rzut = 0


rzut_moneta_n_razy(10)