class BankAccount:
    next_account_id = 1

    #drukowanie sposob 1
    def __str__(self):
        return str(vars(self))

    def __init__(self, owner, password, balance=0):
        self.id = self.next_account_id
        self.owner = owner
        self.password = password
        self.balance = balance
        BankAccount.next_account_id += 1

    #drukowanie sposob 2
    def print_account_self(self):
        for key, value in vars(self).items():
            print(key, value)

    def set_balance(self, new_balance):
        if isinstance(new_balance, (int, float)):
            self.balance = new_balance
        else:
            print('Nowy balans musi byc intem')