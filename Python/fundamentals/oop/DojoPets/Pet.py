class Pet:
    def __init__(self, name, type , tricks, sound, treats, pet_food):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 100
        self.health = 100
        self.sound = sound
        self.treats = treats
        self.pet_food = pet_food
        print (self.name + " Created")
        print (self.name + " is a " + self.type + ".")
        print (self.name + " can " + self.tricks + ".")
        print (self.name + " eats " + self.pet_food + ".")
        print (self.name + " loves " + self.treats + ".")
        print(" ")

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5

    def noise(self):
        print(self.sound)

class Dog(Pet):
    def __init__(self, name, type = "dog", tricks = "roll over", sound = "woof", treats = "Beggin Strips", pet_food = "kibble"):
        super().__init__(name, type, tricks, sound, treats, pet_food)

class Cat(Pet):
    def __init__(self, name, type = "cat", tricks = "attack", sound = "meow", treats = "catnip", pet_food = "cat food"):
        super().__init__(name, type, tricks, sound, treats, pet_food)