# tuplas são estáticas, imutáveis, não podem ser alteradas

tupla1 = tuple()

print(type(tupla1))

tupla2 = (1, 23.5, [1, 2, 45], 'curso', 'django pro', 1)
print(tupla2)

print(dir(tupla2))

print(tupla2.count(1)) #conta quantos elementos da tupla têm o valor passado no parâmetro

tupla2[2].append('kk adicionei mane') #apesar da tupla não poder ser alterada, as listas dentro das tuplas podem ser alteradas

for i in tupla2:
    print(i)