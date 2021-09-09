"""
Napisz funkcję która zwróci True jezeli lista zawiera duplikaty.

[1,2,3,4,1,1,6,6,5]

"""

def list_duplicate_checker(list_given):
    for idx in range(len(list_given)):
        if list_given.count(list_given[idx]) > 1:
            return True
    return False


if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 1, 1, 6, 6, 5]
    list_duplicate_checker(test_list)

