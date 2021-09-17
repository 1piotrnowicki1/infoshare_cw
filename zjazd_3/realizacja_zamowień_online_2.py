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

def do_realizacji(stany_magazynowe: dict, zamawiany_towar: str, ilosc_zamawianych_sztuk: int):
    return stany_magazynowe.get(zamawiany_towar, -1) > ilosc_zamawianych_sztuk

if __name__ == '__main__':
    print(do_realizacji({'bluzka': 5, 'spodnie': 3}, 'spodnie', 2))
    print(do_realizacji({'bluzka': 5, 'spodnie': 3}, 'spodnie', 4))