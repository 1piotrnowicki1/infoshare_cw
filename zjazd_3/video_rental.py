"""
Opcje administratora:
 - Utworzenie nowego uzytkownika
 - Dodanie filmu do bazy danych
 - Modyfikacja filmów w bazie danych

Opcje użytkownika:
 - Zobaczenie oferty
 - Sprawdzenie dostępności filmu
 - Wypożyczene filmu

"""

users = {'admin': '1234', 'user': '12345'}
movies = {'a': {"price": 1, "quantity": 3}, 'b': {'price': 2, 'quantity': 5}}

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
    while True:
        if user_authenticated == 'admin':
            print('Wyberz co chciałbyś zrobić:')
            print('1. Utwórz nowego uzytkownika')
            print('2. Dodaj film do bazy danych')
            print('3. Zmodyfikuj film w bazie danych')
            print('4. Zobacz filmy w bazie danych')
            print('0. Wyjdz z programu')
            option = input("Podaj numer opcji: ")
            if option == '1':
                print(users)
                # krok 1: pryjac dane nowego uzytkownika
                login = input('Podaj nazwe uzytkownika: ')
                password = input('Podaj haslo uzytko0wnika: ')
                # krok 2: zapisac nowego uzytkownika w 'bazie danych'
                users[login] = password
                print(users)
            elif option == '2':
                title = input('Podaj tytul filmu: ')
                price = int(input('Podaj cene filmu: '))
                movies[title] = price
            elif option == '3':
                # krok1: Przyjac dane na temat tytulu filmu
                title = input('Podaj tytul filmu ktory chcialbys zmodyfikowac: ')
                # krok2: sprawdzic czy podany tytul znajduje sie w bazie danych
                if title in movies:
                    pass
                else:
                    print('Film o podanym tytule nie znajduje sie w bazie danych')

            elif option == '4':
                #print(movies)
                [print(key, val) for key, val in movies.items()]
                input('Nacisnij enter, aby wrocic do glownego menu')
            elif option == '0':
                break
        else:
            print('Wyberz co chciałbyś zrobić:')
            print('1. Zobacz oferte')
            print('2. Sprawdz dostepnosc filmu')
            print('3. Wypozycz film')
            print('0. Wyjdz z programu')
            option = input("Podaj numer opcji: ")
            if option == '1':
                [print(key, val) for key, val in movies.items()]
                input('Nacisnij enter, aby wrocic do glownego menu')
            elif option == '2':
                # krok1: Przyjac dane na temat tytulu filmu
                title = input('Podaj tytul filmu ktory chcialbys wypozyczyc: ')
                # krok2: sprawdzic czy podany tytul znajduje sie w bazie danych
                if title in movies:
                    print(f'Film {title} jest dostępny')
                    input('Nacisnij enter, aby wrocic do glownego menu')
                else:
                    print(f'Film {title} nie jest dostępny')
                    input('Nacisnij enter, aby wrocic do glownego menu')
            elif option == '3':
                pass
            elif option == '0':
                break


if __name__ == "__main__":
    main()