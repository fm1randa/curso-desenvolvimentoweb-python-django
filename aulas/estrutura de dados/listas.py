lista1 = list() # cria lista vazia
#print(type(lista1))

lista1.append(1)
#print(lista1)

lista1.append('estrutura')
#print(lista1)

lista2 = [] # cria lista vazia
#print(lista2)

lista2.append(2)
#print(lista2)

lista2.append('de dados')
#print(lista2)

lista1.extend(lista2) # adiciona o conteúdo de uma lista à outra lista
#print(lista1)
#print(lista2)

lista3 = [1, 2, 3, ['lista dentro de lista', 10, 23], 'curso', 'django pro', 1.23]
#print(lista3)   

#print(lista3[3][0])

for i in lista3:
    if (type(i) == list):
        for y in i:
            print(y)
    else:
        print(i)

lista4 = []
for l in range(11):
    lista4.append(l)
    print(lista4)

lista4.pop() # deleta o ultimo item da lista
print(lista4)

lista4.insert(1, 10) # em uma determinada posição, insere um valor (não exclui o valor contido anteriormente, mas o "empurra" pro lado)
print(lista4)

print(dir(lista4))

#lista4.insert(5, 'eu')
lista4.sort() # ordena (ordem crescente) os numeros de uma lista (se contiver apenas números)
#print(lista4)

lista4.reverse() # inverte a ordem dos itens (primeira posicao para ultima posicao, segunda pra penultima...)
print(lista4)

numeros = [n for n in range(6)]
print(numeros)