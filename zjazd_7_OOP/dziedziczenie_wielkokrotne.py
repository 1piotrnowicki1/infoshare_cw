class Parent1:
    hair_color = 'black'
    eye_color = 'green'

    def funkcja_parent1(self):
        print('To jest funkcja odziedziczona z parenta 1')

class Parent2:
    hair_color = 'brown'
    eye_color = 'blue'

    def funkcja_parent2(self):
        print('To jest funkcja odziedziczona z parenta 2')

class Kid(Parent1, Parent2):
    eye_color = Parent2.eye_color
    def funkcja_kid(self):
        print('To jest funkcja dziecka')
#    def __init__(self):
#        print(super().hair_color)

class KidKid(Kid):
    def __init__(self):
        print(super().hair_color)


# POLIMORFIZM
kidkid = KidKid()
print(isinstance(kidkid, Parent1))
print(isinstance(kidkid, Parent2))
print(isinstance(kidkid, Kid))



# kidkid = KidKid()

# kid = Kid()
# print(kid.hair_color)

# kid.funkcja_parent1()
# kid.funkcja_parent2()

# Method resolution order
# kid = Kid()
# print(Kid.__mro__)
