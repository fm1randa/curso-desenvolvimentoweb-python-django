from classes import soma
from carro import Carro
from pessoa_fisica import PessoaFisica

print(soma(1,2))

carro1 = Carro(1.5, 'hidraulica', True, 'Volkswagen')
print(carro1.motor)
print(carro1.eletrico)
print(carro1.partida())
print(carro1.acelera())
print(carro1.parar())

filipe = PessoaFisica('Filipe', 'RM182', None, '14/09/2001')
print(filipe.validar_cpf(filipe.cpf))