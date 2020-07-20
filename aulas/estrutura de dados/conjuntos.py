# não adiciona elementos duplicados

c1 = set()
print(type(c1))

c1.add(1)
print(c1)

c1.add('eu')
print(c1)

c1.add(1)
print(c1)

c1.clear()
print(c1)

c1 = {1, 2, 3, 4, 4, 5, 5}
print(c1, type(c1))

#c1['eu'] = 'Filipe' --- erro TypeError: 'set' object does not support item assignment

c1.pop()
print(c1)

#c1[0] --- não suporta indexação

lista1 = [1, 2, 3, 4]
lista2 = [1, 3, 4, 5, 6, 7]
print(set(lista1).intersection(lista2))

lista3 = [1, 1, 2, 3, 4, 4, 5, 5]
c3 = set(lista3)

print(c3)