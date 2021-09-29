"""
Opcje administratora:
 - Utworzenie nowego uzytkownikaok
 - Dodanie filmu do bazy danych
 - Modyfikacja filmów w bazie danych

Opcje użytkownika:
 - Zobaczenie oferty
 - Sprawdzenie dostępności filmu
 - Wypożyczene filmu

"""


users = {'admin': '1234', 'user': '12345'}
movies = {'a': {"price": 1, "quantity": 3}, 'b': {'price': 2, "quantity": 5}}

def authenticate_user():
    login = input('Podaj nazwe uzytkownika: ')
    if users.get(login):
        password = input('Podaj haslo: ')
        if users[login] == password:
            return login
        else:
            return False
    else:
        return False

def main():
    user_authenticated = False
    while not user_authenticated:
        user_authenticated = authenticate_user()
        print(f'user_authenticated: {user_authenticated}')
    while True:
        if user_authenticated == 'admin':
            print('Wybierz co chciałbyś zrobić:')
            print('1. Utwórz nowego uzytkownika')
            print('2. Dodaj film do bazy danych')
            print('3. Zmodyfikuj film w bazie danych')
            print('4. Zobacz filmy w bazie danych')
            print('0. Wyjdz z programu')
            option = input("Podaj numer opcji: ")

            if option == '1':
                # krok 1: przyjac dane nowego uzytkownika
                login = input('Podaj nazwe uzytkownika: ')
                password = input('Podaj haslo uzytkownika: ')
                # krok 2: zapisac nowego uzytkownika w 'bazie danych'
                users[login] = password

            elif option == '2':
                # krok1: przyjac dane nowego filmu
                title = input('Podaj tytul filmu: ')
                price = int(input('Podaj cene filmu: '))
                quantity = int(input('Podaj ilość fimów: '))
                # krok2: zapisac nowego uzytkownika w 'bazie danych'
                movies[title] = {"price": price, "quantity": quantity}

            elif option == '3':
                # krok1: przyjac dane na temat tytulu filmu
                title = input('Podaj tytul filmu ktory chcicalbys zmodyfikowac')
                # krok2: sprawdzic czy podany tytul znajduje sie w bazie danych
                if title in movies:
                    pass
                else:
                    print('Film o podanym filmie nie znajduje sie w bazie danych')

            elif option == '4':
                print(movies)
                input('Nacisnij enter, aby wrocic do glownego menu')
            elif option == '0':
                break
        else:
            print('Wybierz co chciałbyś zrobić:')
            print('1. Zobacz oferte')
            print('2. Sprawdz dostepnosc filmow')
            print('3. Wypozycz film')
            print('4. Zobacz filmy w bazie danych')
            option = input("Podaj numer opcji: ")

            if option == '1':
                print(movies)
                input('Nacisnij enter, aby wrocic do glownego menu')

            elif option == '2':
                title = input("Podaj tytul szukanego filmu: ")
                if title in movies:
                    print(f'{title} jest dostepny')
                else:
                    print(f'{title} nie jest dostepny')
            elif option == '3':
                # krok1: przyjac dane na temat tytulu filmu
                title = input('Podaj tytul filmu ktory chcicalbys wypozyczyc')
                # krok2: sprawdzic czy podany tytul znajduje sie w bazie danych
                if title in movies:
                    if movies[title]['quantity'] > 0:
                        print("Film wypozyczony ")
                        movies[title]['quantity'] -= 1
                    else:
                        print(f'Film {title} nie jest doostepny')
                else:
                    print('Film o podanym filmie nie znajduje sie w bazie danych')

            elif option == '4':
                print(movies)
                input('Nacisnij enter, aby wrocic do glownego menu')
            elif option == '0':
                break

if __name__ == "__main__":
    main()