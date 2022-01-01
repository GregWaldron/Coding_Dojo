class BankAccount:

    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            self.balance -= 5
            print ("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print ("Interest Rate: " + str(self.int_rate) + "  Balance: " + str(self.balance))
        return self

    def yield_interest(self):
        print (self.int_rate)
        return self

    @classmethod
    def show_accounts(cls):
        for account in cls.all_accounts:
            print ("Interest Rate: " + str(account.int_rate) + "  Balance: " + str(account.balance))
        return sum

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

account1 = BankAccount(.025, 752000)
account2 = BankAccount(.021, 81093)

account1.deposit(897).deposit(2915).deposit(88).withdraw(500000).yield_interest().display_account_info()
account2.deposit(1000).deposit(10000).withdraw(50).withdraw(114).withdraw(85).withdraw(400).yield_interest().display_account_info()

print(" ")
print("Full Account List")
BankAccount.show_accounts()