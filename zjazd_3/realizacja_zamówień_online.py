"""
Jesteś właścicielem/-elką małego biznesu który prowadzisz online i dużą częścią Twojego dnia jest realizacja zamówień.
Żeby ułatwić swoją pracę, postanowiłeś/-aś napisać funkcję, która pomoże zdecydować czy realizacja zamówienia jest możliwa.

Funkcja przyjmie trzy argumenty:
 - towar: dict – słownik reprezentujący cały towar którym dysponuje Twój biznes
 - zamowienie: string – string reprezentujący towar który chce zamówić klient
 - n: int – liczba reprezentująca ile sztuk chce zamówić klient

Funkcja ma zdecydować, czy Twój sklep jest w stanie wykonać zamówienie.
do_realizacji({‘bluzka’: 5, ‘spodnie’: 3}, ‘spodnie’, 2) -> True
do_realizacji(({‘bluzka’: 5, ‘spodnie’: 3}, ‘spodnie’, 4) - False
"""

towar = {'bluzka': 5, 'spodnie': 3}

def sklep(towar, zamowienie, n):
    if zamowienie in towar:
        if towar[zamowienie] >= n:
            print("True")
        else:
            print("False")
    else:
        print("nie ma towaru")

sklep({'bluzka': 5, 'spodnie': 7}, 'spodnie', 4)