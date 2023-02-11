import pets

class Ninja:
    def __init__(self,first_name,last_name,pet):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        
    def walk(self):
        print(f'Time to go walk! Walking {self.pet}')
        return self
    
    def feed(self):
        print(f'Time to eat! Feeding {self.pet}')
        return self
    
    def bathe(self):
        print(f'Bath time! washing {self.pet}')
        return self
    
ninja_lukas = Ninja('Lukas', 'Hart', pets.pet1.name)

ninja_lukas.walk().feed().bathe()