# Sprsób 1: przekazanie list jako parametry/argumenty

def dodaj_listy(lista1, lista2):
    if len(lista1) != len(lista2):
        print('Podane listy sa roznej dlugosci')
    else:
        lista_sum = []
        for i in range(len(lista1)):
            suma = lista1[i] + lista2[i]
            lista_sum.append(suma)
        return lista_sum

lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista3 = [1,2,3]

#print(dodaj_listy(lista1, lista2))
#print(dodaj_listy(lista1, lista3))


# Sposób 2: przekazanie list jako input od uzytkownika

def dodaj_listy_input():
    raw_input1 = input('Podaj liste liczb oddzielonych od siebie przecinkiem: ')
    raw_input2 = input('Podaj liste liczb oddzielonych od siebie przecinkiem: ')

    # rodzielanie string oddzielonych przecinkime od Sb liczb
    raw_list1 = raw_input1.split(',')
    raw_list2 = raw_input2.split(',')

    stripped_list1 = [element.strip() for element in raw_list1]
    stripped_list2 = [element.strip() for element in raw_list2]

    int_list1 = [int(element) for element in stripped_list1]
    int_list2 = [int(element) for element in stripped_list2]

    print(f'raw_input1: {raw_input1}')
    print(f'raw_input2: {raw_input2}')
    print(f'raw_list1: {raw_list1}')
    print(f'raw_list2: {raw_list2}')
    print(f'stripped_list1 = {stripped_list1}')
    print(f'stripped_list2 = {stripped_list2}')
    print(f'int_list1: {int_list1}')
    print(f'int_list2: {int_list2}')

    #list comprehension
    # final = [int(element) for element in [element.strip() for element in raw_input1.split(',')]]
    # print(final)
dodaj_listy_input()


