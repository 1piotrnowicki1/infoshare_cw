class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Animal is speaking')

animal = Animal('Lion')
animal2 = Animal('Tiger')
animal.speak()
animal2.speak()

# class Rower:
#     def __init__(self, color):
#         self.wheels = 4
#         self.color = color
#
# animal = Animal('Lion')
# animal2 = Animal('Tiger')
# animal3 = Animal('Cat')
# print(animal.name)
# print(animal2.name)
# print(animal3.name)
# rower = Rower(color='blue')
# print(rower.color)
# print(rower.wheels)