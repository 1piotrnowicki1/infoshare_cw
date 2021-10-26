class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
        self.has_fur = True

    def drink_milk(self):
        print('Drinking milk')

class Dog(Mammal):
    def __init__(self, name, species):
        super().__init__(name, species)
        self.has_4_legs =  True

dog = Dog('Burek', 'pies')
print(dog.name, dog.species, dog.has_fur, dog.has_4_legs)

