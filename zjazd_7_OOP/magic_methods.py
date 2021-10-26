class Example:
    def __init__(self, number):
        self.number = number
        self.x = 'x'
        self.y = 'y'

    def __add__(self, example_object):
        return self.number + example_object.number

    def __str__(self):
        return f'To jest obiekt klasy Example którego wartością jest {self.number}'

    def __setattr__(self, name, value):
        if not isinstance(value, int):
            print('Niestety, błąd')
        else:
            print('Ok, zmieniam')
            self.__dict__[name] = value


ex1 = Example(1)
ex2 = Example(3)
ex1.x = 'cokolwiek'
ex1.x = 10
print(ex1.x)


# print(ex1.number)
# print(ex2.number)
# print(ex1 + ex2)
# ex1_dicted = ex1.__dict__
# print(ex1_dicted.get('x'))


