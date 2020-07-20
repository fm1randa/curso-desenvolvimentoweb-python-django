import random

print(random.randint(1, 10))
print(random.random()*100)

alunos = ['jose', 'maria', 'joao', 'francisco', 'paulo', 'diego']
random.shuffle(alunos)
print(alunos)
pick = random.randint(0, len(alunos)-1)
print('Numero escolhido: {}'.format(pick))
print('Aluno sorteado: {}'.format(alunos[pick]))

#acabei de descobrir que existe o metodo choice() D:

print(random.choice(alunos))
