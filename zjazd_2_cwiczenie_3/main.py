lista = [1, 2, 3, 4]

print(lista[0])
print(lista.index(2))
lista = lista + [4]
print(lista)

lista.insert(0,10)
print(lista)

lista.append(9)
print(lista)

lista.extend([0, 1, 0, 1])
print(lista)

print(lista.count(1))

lista.sort()
print(lista)