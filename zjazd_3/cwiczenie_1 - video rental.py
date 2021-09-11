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

def authenticate_user():
    login = input('Podaj nazwe uzytkownika: ')
    password = input('Podaj haslo: ')
    if users.get(login):
        if users[login] == password:
            return True
        else:
            return False
    else:
        return False

def main():
    user_authenticated = False
    while not user_authenticated:
        user_authenticated = authenticate_user()
        print(f'user_authenticated: {user_authenticated}')
    if user_authenticated == 'admin':
        print('Wybierz co chciałbyś zrobić:')
        print('1. Utwórz nowego uzytkownika')
        print('2. Dodaj film do bazy danych')
        print('3. Zmodyfikuj film w bazie danych')
        print('4. Zobacz filmy w bazie danych')
        option = input("Podaj numer opcji: ")
        if option == '1':
            print(users)
            # krok 1: przyjac dane nowego uzytkownika
            login = input('Podaj nazwe uzytkownika: ')
            password = input('Podaj haslo uzytkownika: ')
            # krok 2: zapisac nowego uzytkownika w 'bazie danych'
            user[login] = password
            print(users)
        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            pass
    else:
        print('Wybierz co chciałbyś zrobić:')
        print('1. Zobacz oferte')
        print('2. Sprawdz dostepnosc filmow')
        print('3. Wypozycz film')
        print('4. Zobacz filmy w bazie danych')
        option = input("Podaj numer opcji: ")

if __name__ == "__main__":
    main()