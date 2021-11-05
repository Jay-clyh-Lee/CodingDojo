class User:

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdraw(self, amount):
        self.account_balance -= amount
        return self
        
    def display_user_balance(self):
        print(self.account_balance)

    def transfer_money(self, amount, recipient):
        self.account_balance -= amount
        recipient.account_balance += amount

monty = User('monty', 'monty@gmail.com')
python = User('python', 'python@gmail.com')
google = User('google', 'google@gmail.com')

monty.make_deposit(1000).make_deposit(10000).make_deposit(100000).make_withdraw(5000).display_user_balance()

python.make_deposit(100000).make_deposit(5000).make_withdraw(500110).make_withdraw(50000).display_user_balance()

google.make_deposit(5001101).make_withdraw(50000).make_withdraw(500110).make_withdraw(50000).display_user_balance()