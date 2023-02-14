class User:
    
    def __init__(self,first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        
    def display_info(self):
        print(f'{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.gold_card_points}')
        return self

    def enroll(self):
        command = input('Would you like to enroll? type "yes" or "No" -->  ').lower()
        if command == "yes":
            self.is_rewards_member = True
            self.gold_card_points += 200
            print(f'You have been enrolled and {self.gold_card_points} points have been added to your account')
        else:
            print('You have selected to not enroll in the goldcard program')
        return self
        
    def spend_points(self,amount):
        if self.gold_card_points < amount:
            print("You don't have enough points")
        else:
            self.gold_card_points -= amount
            print(f'You spent {amount} points and have {self.gold_card_points} points remaining.')
        return self
        
user_1 = User('Lukas','Hart', 'email@email.com', 29)
user_2 = User('T','f','tf@email.com', 29)
user_3 = User('L','h','email@email.com', 21)

user_1.display_info().enroll().spend_points(200)

