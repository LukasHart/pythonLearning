class Pet:
    def __init__(self,name,type,tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0
        
    def sleep(self):
        self.energy += 25
        print('Pet sleeps and gains 25 energy')
        return self
    
    def eat(self):
        self.energy += 5 
        self.health += 10
        print('Pet eats and gains 5 energy and 10 health')
        return self
    
    def play(self):
        self.health +=5
        print('your pet plays and gains 5 health')
        return self
    
    def noise(self):
        if self.type == 'dog':
            print('Bark!')  
        elif self.type == 'cat':
            print('Meow!') 
        else:
            print('Animal noise!')
            
class OutdoorPets(Pet):
    pass

pet1 = Pet('Tav','Dog', 'tricks')
pet1.eat()