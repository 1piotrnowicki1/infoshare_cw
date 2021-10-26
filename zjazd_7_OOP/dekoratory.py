def error_handler(func):
    def wrapper():
        print('b')
        func()
        print('c')
    return wrapper

@error_handler
def a():
    print('a')

a()
