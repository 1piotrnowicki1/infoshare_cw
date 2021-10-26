

class Example:
    def __init__(self):
        self.y = 'y'
        self.__x = 'x'

    def get_x(self, password):
        if password == '1234':
            return self.__x
        else:
            return 'Niestety, ale złe hasło'

example = Example()
print(example.get_x('12345'))
print(example.y)