from member import Member

class Salon_Samochodowy:

    members = []
    cars = []

    def __init__(self):
        self.main()

    def add_member(self):
        Imie = input('Podaj imie: ')
        Nazwisko = input('Podaj nazwisko: ')
        member = Member(Imie, Nazwisko)
        Salon_Samochodowy.members.append(member)

    def members_list(self):

        for member in Salon_Samochodowy.members:
            print(vars(member))

        #print(Salon_Samochodowy.members)

    def print_menu(self):
        print('Wybierz opcje: ')
        print(10 * '*')
        print('1. Dodaj membera ')
        print('2. Members')



    def main(self):
        while True:
            self.print_menu()
            option = input('Podaj opcję: ')
            if option == '1':
                self.add_member()
            elif option == '2':
                self.members_list()

Salon_Samochodowy()