class Member:

    klient = 1
    def __init__(self, Imie, Nazwisko):
        self.Lp = self.klient
        self.Imie = Imie
        self.Nazwisko = Nazwisko
        Member.klient += 1

