class Example:
    def __init__(self):
        self.y = 'y'
        self.__x = 'x'


    @property
    def x(self):
        print('__x getter was called')
        return ('Ta wartość jest dostępna wewnatrz klasy')

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            print('Podana wartość musi być ustawiona jako int')
        else:
            self.__x = value

    @x.deleter
    def x(self):
        print('Deleting __x')
        del self.__x

    def __add(self):
        return 'add function was called'

    def add(self, password):
        if password == '1234':
            return self.__add()
        else:
            return 'haslo nieprawidlowe'


example = Example()
print(example.add('1234'))
# example.x = 10
# print(example.x)
# print(example.__x)

