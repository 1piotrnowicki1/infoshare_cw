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

