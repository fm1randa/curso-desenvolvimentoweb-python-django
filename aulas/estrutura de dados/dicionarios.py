ctts = dict()

contatos = {}

print(type(contatos))

contatos['joao'] = '8888-9877'
print(contatos)

contatos['jose'] = '3349-9876'
contatos['maria'] = '0207-6876'
contatos['paulo'] = '9879-3490'
contatos[123] = '4567-9087'
print(contatos)

for k, v in contatos.items():
    print('Chave: {} | Valor: {}'.format(k, v))

contatos.pop(123)
print(contatos)

contatos.popitem()
print(contatos)

for k in contatos.keys():
    print(k)

for v in contatos.values():
    print(v)