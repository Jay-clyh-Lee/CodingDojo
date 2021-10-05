class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.account_balance)

    def transfer_money(self, name, amount):
        self.account_balance -= amount
        name.account_balance += amount

Nami = User('Nami', 'Name@onepiece.com')
Zoro = User('Zoro', 'Zoro@onepiece.com')
Luffy = User('Luffy', 'Luffy@onepiece.com')

Nami.make_deposit(1000000).make_deposit(50000).make_deposit(200000).make_withdrawal(1000000).display_user_balance()
Zoro.make_deposit(1000).make_deposit(5000).make_withdrawal(5500).make_withdrawal(10000).display_user_balance()
Luffy.make_deposit(1000000).make_withdrawal(1000000).make_withdrawal(1000000).make_withdrawal(5000000).display_user_balance()

Nami.display_user_balance()
Zoro.display_user_balance()
Nami.transfer_money(Zoro, 10000)
Nami.display_user_balance()
Zoro.display_user_balance()