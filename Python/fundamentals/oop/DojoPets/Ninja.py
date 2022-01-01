import Pet

class Ninja:
    def __init__(self, first_name , last_name , pet, pet_type):
        self.first_name = first_name
        self.last_name = last_name
        print (self.first_name + " " + self.last_name + " Created")
        if pet_type == "Dog":
            self.pet = Pet.Dog(name=pet)
        else:
            self.pet = Pet.Cat(name=pet)
        self.pet_type = pet_type

    def status(self):
        print("Health: " + str(self.pet.health))
        print("Energy: " + str(self.pet.energy))
        print(" ")
        return self

    def walk(self):
        self.pet.play()
        print (self.pet.name + " Walked")
        self.status()
        return self

    def feed(self):
        self.pet.eat()
        print (self.pet.name + " Fed")
        self.status()
        return self
        
    def bathe(self):
        print (self.pet.name + " Bathed")
        self.pet.noise()
        print (" ")
        return self