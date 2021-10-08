# import card
from card import Card
from account import BankAccount
from operation import Operation

class Bank:
    client_list = []
    card_list = []
    operation_history = []
    def __init__(self):
        self.main()

    def print_menu(self):
        print('Wybierz opcje:')
        print(10 * '*')
        print('1. Dodaj kartę')
        print('2. Sprawdź karty')
        print('3. Odczytaj saldo')
        print('4. Dodaj konto bankowe')
        print('5. Pokaz konta bankowe')
        print('6. Wyślij pieniądze')
        print('7. Ustaw balans')
        print('8. Historia operacji')

    def add_operation_history(self, operation: str) -> None:
         """
         Creates an Operation object, then adds it to Bank.operation_history

         Args:
              operation (str): name of the operation
         """
         new_operation = Operation(operation)
         Bank.operation_history.append(new_operation)

    def add_card(self):
        pin = input('Podaj pin: ')
        saldo = input('Podaj saldo: ')
        # card.Card(pin, saldo)
        card = Card(pin, saldo)
        Bank.card_list.append(card)
        self.add_operation_history('New card created')

    def show_cards(self):
        #print(Bank.card_list)
    # def show_cards(self):
    #     [print(str(card.card_number) + '. ' + str(card.saldo)) for card in Bank.card_list]

        for card in Bank.card_list:
            card.print_self()
        self.add_operation_history('Cards information requested')

    def show_card_balance(self):
        # 1. Przyjecie od uzytkownika numeru karty
        card_number = int(input('Podaj numer karty: '))
        # 2. Sprawdzenie czy dany numer karty istnieje
        card_numbers = [card.number for card in self.card_list]
        card_exists = card_number in card_numbers
        # 3. Przyjęcie od uzytkownika numeru PIN
        # 4. Sprawdzenie czy PIN jest zgodny
        # 5. Pokazanie salda / informacja ze PIN jest nieprawidlowy
        if card_exists:
            pin = input('Podaj PIN: ')
            index_card = card_numbers.index(card_number)
            card = self.card_list[index_card]
            if pin == card.pin:
                print(card.saldo)
            else:
                print('PIN nieprawidlowy')
        else:
            print('Nie ma takiej karty')
        #self.add_operation_history('Cards information requested')
        self.add_operation_history('Show balance card requested')

    def add_bank_account(self):
        owner = input('Proszę podać właściciela: ')
        password = input('Proszę podać hasło')
        account = BankAccount(owner, password)
        Bank.client_list.append(account)
        self.add_operation_history('New bank account created')

    def show_operation_history(self):
        for operation in Bank.operation_history:
            print(vars(operation))

    def show_bank_accounts(self):
        # print(Bank.client_list)

        # Sposób 1: __str__
        # for bank_account in Bank.client_list
        #     print(bank_account)

        # Sposób 2: self.print_self()
        for bank_account in Bank.client_list:
            bank_account.print_account_self()
        self.add_operation_history('Show bank account requested')

    def set_account_balance(self):
        def check_if_account_exists(account_id):
            # Jezeli uzytkownik istnieje, zwroc obiekt
            for bank_account in Bank.client_list:
                if bank_account.id == account_id:
                    return bank_account
                else:
                    continue
            # Jezeli uzytkownik nie istnieje, zwroc False
            return False

        # 1. Wybrać konto z którego ma nastąpić przelew
        account_id = int(input('Podaj id konta dla którego chcesz ustawic przelew: '))
        account = check_if_account_exists(account_id)
        if account:
            new_balance = int(input('Podaj balans'))
            account.set_balance(new_balance)
        else:
            print('Wybrane konto nie pasuje')
        self.add_operation_history('Account balance setted')

    def send_money(self):
        def check_if_account_exists(account_id):
            # Jezeli uzytkownik istnieje, zwroc obiekt
            for bank_account in Bank.client_list:
                if bank_account.id == account_id:
                    return bank_account
                else:
                    continue
            # Jezeli uzytkownik nie istnieje, zwroc False
            return False

        # 1. Wybrać konto z którego ma nastąpić przelew
        account_id = int(input('Podaj id konta z którego chcesz wysłać pieniądze: '))
        account = check_if_account_exists(account_id)
        if account:
            # 2. Wybrać sumę i sprawdzić czy jest to mozliwe
            amount = int(input('Podaj ilość pienędzy do wysłania: '))
            if account.balance >= amount:
                # 3. Wybrać konto na które ma pójść przelew
                receiver_account_id = int(input('Podaj id konta na które chcemy wysłać pieniądze: '))
                receiver_account = check_if_account_exists(receiver_account_id)
                if receiver_account:
                    # 4. Wysłać pieniądze
                    account.balance -= amount
                    receiver_account.balance += amount
                else:
                    print('Przepraszamy, ale konto odbiorcy nie istnieje.')
            else:
                print('Przepraszam, niewystarczajaca ilosc pieniedzy')
        else:
            print('Przepraszam, wybrane konto nie istnieje.')
        self.add_operation_history('Transfer money')

    def main(self):
        while True:
            self.print_menu()
            option = input('Podaj opcję: ')
            if option == '1':
                self.add_card()
            elif option == '2':
                self.show_cards()
            elif option == '3':
                self.show_card_balance()
            elif option == '4':
                self.add_bank_account()
            elif option == '5':
                self.show_bank_accounts()
            elif option == '6':
                self.send_money()
            elif option == '7':
                self.set_account_balance()
            elif option == '8':
                self.show_operation_history()


Bank()