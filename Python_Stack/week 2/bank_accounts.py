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
        self.balance -= amount
        return self

    def display_account_info(self): 
        print(f'The account balance is: {self.balance}')

    def yield_interest(self):
        self.balance *= (1 + self.interest_rate)
        return self

    @classmethod
    def print_all(cls):
        for account in cls.accounts:
            print(account)

Michael = BankAccount(.05).deposit(1000).deposit(1000).deposit(1000).withdraw(500).yield_interest().display_account_info()
Gabrial = BankAccount(.05).deposit(1000).deposit(1000).withdraw(300).withdraw(300).withdraw(300).withdraw(300).yield_interest().display_account_info()

BankAccount.print_all()