"""
Napisz funkcję która zwróci True jezeli lista zawiera duplikaty.

[1,2,3,4,1,1,6,6,5]

"""


def lista_duplicate():
    list_given = [1, 2, 3, 4, 4]
    my_set = set(list_given)

    if len(my_set) == len(list_given):
        print("False")
        return False
    else:
        print("True")
        return True

lista_duplicate()