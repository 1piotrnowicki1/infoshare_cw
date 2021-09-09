"""
Problem Collatza - user define number

"""

def collatza():
    liczba = int(input("Podaj pierwszą liczbę: "))

    while liczba != 1:
        if liczba % 2 == 0:
            liczba = (liczba // 2)   #float division
        else:
            liczba = (liczba * 3 + 1)
        print(liczba)

collatza()