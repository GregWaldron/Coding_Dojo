class BankAccount:
    def __init__(self, account_name, int_rate, balance):
        self.account_name = account_name
        self.int_rate = int_rate
        self.balance = balance

class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.user_accounts = []

    def add_account(self, interest, starting_balance):
        self.user_accounts.append (BankAccount(account_name="account" + str(len(self.user_accounts)), int_rate=interest, balance=starting_balance))
        return self

    def make_deposit(self, account_number, amount):
        self.user_accounts[account_number].balance += amount
        print ("Depositing " + str(amount) + " to " + self.user_name + " account" + str(account_number))
        print (" ")
        return self

    def make_withdrawal(self, account_number, amount):
        self.user_accounts[account_number].balance -= amount
        print ("Withdrawing " + str(amount) + " from " + self.user_name + " account" + str(account_number))
        print (" ")
        return self

    def show_user_accounts(self):
        for x in range (0, len(self.user_accounts)):
            print(self.user_name + " " + self.user_accounts[x].account_name + " balance: " + str(self.user_accounts[x].balance))
        print(" ")
        return self

jessica = User("Jessica Waldron")
jessica.add_account(.02, 50).add_account(.02, 150).show_user_accounts().make_deposit(0, 300).make_withdrawal(1, 100).show_user_accounts()

kaitlyn = User("Kaitlyn Waldron")
kaitlyn.add_account(.02, 85).add_account(.02, 400).add_account(.02, 8000).show_user_accounts().make_deposit(0, 300).make_deposit(1, 480).make_deposit(2, 1347).make_withdrawal(1, 100).make_withdrawal(2, 10).show_user_accounts()