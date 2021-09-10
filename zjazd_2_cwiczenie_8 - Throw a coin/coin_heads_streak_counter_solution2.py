"""
Napisz funkcję która:
 - Symuluje rzut monetą
 - Rzuca monetą określoną ilość razy i zwraca najdłuższy ciąg orlów

Zeby bylo prosciej, mozecie przyjac ze wartosc Reszki to 0, a orła 1

"""

import random

def rzuc_moneta():
    return random.choice([0,1])

def policz_orly(n):
    current_run, longest_run = 0
    orzel_w_poprzednim_rzucie = None
    for i in range(n):
        #Python traktuje liczbe 1 jako True, liczbe 0 jako False
        wypadl_orzel = rzuc_moneta()
        if wypadl_orzel and (orzel_w_poprzednim_rzucie or orzel_w_poprzednim_rzucie is None):
            # Pytanie: dlaczego jest orzel_w_poprzednim_rzucie is None?
            # Odpowiedz: Bo przed rozpoczeciem rzucania moneta, nie mozemy zdefiniowac czym byl poprzedni rzut.
            # Jest to wspomniany na zajeciach 'warunek startowy'
            current_run += 1
        else:
            longest_run = max(longest_run, current_run)
            current_run = 0
        orzel_w_poprzednim_rzucie = wypadl_orzel
    return longest_run