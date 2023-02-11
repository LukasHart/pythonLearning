class User:

    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f'First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nAge: {self.age}\nIs rewards member: {self.is_rewards_member}\nTotal gold card points: {self.gold_card_points}')
        return self

    def enroll(self):
        self.gold_card_points = 200
        if self.is_rewards_member == True:
            print('User is already a rewards member.')
        else:
            self.is_rewards_member == True
            print('You have been enrolled. ')
        return self
    
    def spend_points(self,amount):
        self.gold_card_points = self.gold_card_points - amount
        if self.gold_card_points <=0:
            print('You do not have enough points')
        else:
            print(f'You spent {amount} points and have {self.gold_card_points} points remaining.')
        return self


User1 = User('Lukas', 'Hart', 'email@email.com', 29)
User2 = User('Cami', 'Dunbar', 'email@email.com', 21)
User3 = User('Tim', 'Bob', 'moreemail@email.com', 44)


User1.enroll().spend_points(50).display_info()

User2.enroll().spend_points(80).display_info()

User3.enroll().spend_points(200).display_info()

