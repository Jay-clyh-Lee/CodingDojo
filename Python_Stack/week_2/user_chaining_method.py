class BankAccount:

    accounts = []

    def __init__(self, interest_rate, balance = 0) -> None:
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print(f"Not enough funds in account. Current balance: {self.balance}")
        return self

    def display_account_info(self): 
        print(f'The account balance is: {self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.interest_rate)
            print(f"Not enough funds in account. Current balance: {self.balance}")
        return self

    @classmethod
    def print_all(cls):
        for account in cls.accounts:
            account.display_account_info()


class User:

    user_accounts = []

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.account = BankAccount(.05, 0)
        self.user_accounts.append(BankAccount(.05, 0))

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self
        
    def display_user_balance(self):
        self.account.display_account_info()

    def transfer_money(self, amount, recipient):
        self.account.withdraw(amount)
        recipient.account.deposit(amount)

FengJiu = User('monty', 'monty@gmail.com')
BambooGreenSnake = User('python', 'python@gmail.com')
Lily = User('google', 'google@gmail.com')

FengJiu.make_deposit(1000).make_deposit(10000).make_deposit(100000).make_withdraw(5000).display_user_balance()
BambooGreenSnake.make_deposit(100000).make_deposit(5000).make_withdraw(500110).make_withdraw(50000).display_user_balance()
Lily.make_deposit(5001101).make_withdraw(50000).make_withdraw(500110).make_withdraw(50000).display_user_balance()

Lily.transfer_money(500, FengJiu)
Lily.display_user_balance()
FengJiu.display_user_balance()