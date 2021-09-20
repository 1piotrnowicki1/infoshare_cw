    class Example:
        pass


    class Example2:
        def __init__(self):
            print('Starting initialization...')
            self.name = 'Instance of Example2 class'
            print('Doing somethign...')
            print('Finished initialization.')


        def funkacja(self):
            print('Printing something')

    example2 = Example2()
    example3 = Example2()
    print(example2.name)
    example2.funkacja()
