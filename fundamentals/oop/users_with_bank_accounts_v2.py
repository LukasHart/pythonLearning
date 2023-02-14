class User:
    def __init__(self,name,email,acc_type):
        self.name = name
        self.email = email
        self.acc_type = acc_type
        self.account = BankAccount()

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def display_account_info(self):
        print(self.acc_type)
        self.account.display_account_info()
        return self
        
    def withdraw(self,amount):
        self.account.withdraw(amount)
        return self
        
class BankAccount:
    def __init__(self):
        self.int_rate = 0.15
        self.balance = 0
        
    def deposit(self,amount):
        self.balance += amount
        print(f"${amount} has been deposited to your account")
        return self
    
    def withdraw(self,amount):
        if self.balance < amount:
            balance_after_fee = self.balance - 5
            print('Tried to withdraw more than available charging a $5 fee')
            print(f'Your balance is ${balance_after_fee}')
        else:
            self.balance -= amount
            print(f'${amount} withdrawn from your account')
        return self
    
    def display_account_info(self):
        print(f"Your account balance is ${self.balance}\nYour account's interest rate is ${self.int_rate}")
        return self
    
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        print(f'Yielded Interest is ${self.balance}')
        return self
    
checking = User('Lukas','email@email.com','checking')
savings = User('Lukas','email@email.com','savings')

checking.make_deposit(2500)
savings.make_deposit(10000)

checking.withdraw(1500)
savings.withdraw(5000)


checking.display_account_info()
savings.display_account_info()