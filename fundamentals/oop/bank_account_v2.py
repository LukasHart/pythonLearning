class BankAccount:
    accounts = []
    def __init__(self):
        self.int_rate = 0.19
        self.balance = 0
        BankAccount.accounts.append(self)
    
    
    @classmethod
    def all_accounts(cls):
        for account in cls.accounts:
            print(f'This accounts interest rate is: {account.int_rate} %, This accounts balance is: {account.balance}')
    
    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} has been deposited to your account")
        return self
    
    def withdraw(self,amount):
        if self.balance < amount:
            balance_after_fee = self.balance - 5
            print('Tried to withdraw more than available charging a $5 fee')
            print(f'Your balance is ${balance_after_fee}')
        else:
            self.balance -= amount
            print(f'{amount} withdrawn from your account')
        return self
    
    def display_account_info(self):
        print(f"Your account balance is ${self.balance}\nYour account's interest rate is ${self.int_rate}")
        return self
    
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        print(f'Yielded Interest is ${self.balance}')
        return self
    
user_1 = BankAccount()
user_2 = BankAccount()

user_1.deposit(500).withdraw(250).yield_interest().display_account_info()
BankAccount.all_accounts()