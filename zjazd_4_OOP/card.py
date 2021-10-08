class Card:
    provider = 'MasterCard'
    last_number = 1

    def __init__(self, pin, saldo):
        self.number = self.last_number
        self.pin = pin
        self.saldo = saldo
        Card.last_number += 1

    def change_pin(self):
        self.pin = int(input('Podaj nowy nr PIN: '))

    def print_self(self):
        for key, value in vars(self).items():
            print(key, value)







    # def change_saldo(self):
    #     self.saldo = int(input('Podaj nowe saldo: '))

# def create_card():
#     pin = input('Podaj number PIN: ')
#     saldo = input('Podaj saldo: ')
#     card = Card(pin=pin, saldo=saldo)
#     return card

# card = create_card()
# card.change_pin()
# card.change_saldo()
# print(card.pin)
# print(card.saldo)