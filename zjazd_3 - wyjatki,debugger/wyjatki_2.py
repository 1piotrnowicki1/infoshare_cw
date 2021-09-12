# import sys
# try:
#     foo = int(input('podaj liczbe: '))
#     print('Wpisales ', foo)
#
#
# except TypeError:
#     print('Jakis blad')
# except:
#     print('Nieoczekiwany blad', sys.exc_info()[0])

try:
    foo = int(input('podaj liczbe: '))
except ValueError:
    print('Nie wpisales liczby')
    raise
else:
    print('wpisales ', foo)
