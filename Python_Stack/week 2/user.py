class User:

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdraw(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.account_balance)

    def transfer_money(self, amount, recipient):
        self.account_balance -= amount
        recipient.account_balance += amount

monty = User('monty', 'monty@gmail.com')
python = User('python', 'python@gmail.com')
google = User('google', 'google@gmail.com')

monty.make_deposit(1000)
monty.make_deposit(10000)
monty.make_deposit(100000)
monty.make_withdraw(5000)
monty.display_user_balance()

python.make_deposit(100000)
python.make_deposit(5000)
python.make_withdraw(500110)
python.make_withdraw(50000)
python.display_user_balance()

google.make_deposit(5001101)
google.make_withdraw(50000)
google.make_withdraw(500110)
google.make_withdraw(50000)
google.display_user_balance()

monty.display_user_balance()
python.display_user_balance()
google.display_user_balance()

google.transfer_money(500000, python)
google.display_user_balance()
python.display_user_balance()
