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

Michael = BankAccount(.05).deposit(1000).deposit(1000).deposit(1000).withdraw(500).yield_interest().display_account_info()
Gabrial = BankAccount(.05).deposit(1000).deposit(1000).withdraw(300).withdraw(300).withdraw(300).withdraw(300).yield_interest().display_account_info()

BankAccount.print_all()