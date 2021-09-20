class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Animal is speaking')

animal = Animal('Lion')
animal2 = Animal('Tiger')
animal.speak()
animal2.speak()