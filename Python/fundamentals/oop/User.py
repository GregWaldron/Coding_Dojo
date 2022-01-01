class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print (self.name + ": " + str(self.account_balance))

    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount

jessica = User("Jessica Waldron", "jessica@email.com")
kaitlyn = User("Kaitlyn Waldron", "kaity@email.com")
daniel = User("Daniel Pickett", "dan@email.com")

jessica.make_deposit(464)
jessica.make_deposit(222)
jessica.make_deposit(110)
jessica.make_withdrawal(23)
jessica.display_user_balance()

kaitlyn.make_deposit(1012)
kaitlyn.make_deposit(1999)
kaitlyn.make_withdrawal(805)
kaitlyn.make_withdrawal(303)
kaitlyn.display_user_balance()

daniel.make_deposit(6900)
daniel.make_withdrawal(330)
daniel.make_withdrawal(2010)
daniel.make_withdrawal(11)
daniel.display_user_balance()

jessica.transfer_money(daniel, 42)

jessica.display_user_balance()
daniel.display_user_balance()