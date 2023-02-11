class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = 0
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'${amount} Has been deposited to your account, current balance is ${self.balance}')
        return self

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(
            f'${amount} Has been withdrawn from your account. your reamining balance is ${self.balance}')
        return self

    def display_account_info(self):
        print(
            f'-Your account info-\nUsers interest rate: {self.int_rate} %\nCurrent balance: ${self.balance}')
        return self

    def yield_interest(self,int_rate):
        self.balance += self.balance * int_rate
        print(f'Yielded Interest is ${self.balance}')
        return self
    
    @classmethod
    def show_accounts(cls):
        for account in cls.all_accounts:
            print(account.__dict__)

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.19, balance = 0)
    
    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self,amount):
        self.account.withdraw(amount)
        return self

    def display_user(self):
        self.account.display_account_info()


user1 = User('Lukas', 'email@email.com')
user1.make_deposit(500).make_withdrawl(250).display_user()

# account1 = BankAccount(0.1, 0)
# account2 = BankAccount(0.19, 0)
# account3 = BankAccount(0.15,0)

# account1.deposit(500).deposit(250).deposit(
#     50).withdraw(400).yield_interest(0.01).display_account_info()

# account2.deposit(100).deposit(50).withdraw(25).withdraw(17).withdraw(5).withdraw(50).yield_interest(0.19).display_account_info()

# BankAccount.show_accounts()
