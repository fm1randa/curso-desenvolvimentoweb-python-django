'''
from classes import soma
from carro import Carro
from pessoa_fisica import PessoaFisica
'''
#print(soma(1,2))
'''
carro1 = Carro(1.5, 'hidraulica', True, 'Volkswagen')
print(carro1.motor)
print(carro1.eletrico)
print(carro1.partida())
print(carro1.acelera())
print(carro1.parar())
'''

'''
filipe = PessoaFisica('Filipe', 'RM182', None, '14/09/2001')
print(filipe.validar_cpf(filipe.cpf))
'''
'''
from conta import Conta
from agencia import Agencia
from pessoa import Pessoa

p1 = Pessoa('Filipe', 'RM182')
print(p1._nome)
a1 = Agencia('12345-6')
c1 = Conta('123-45', a1, p1, 0.0)

print(c1.get_cliente())
print(c1._agencia._numero)
'''

from pessoa import Pessoa
from pessoa_fisica import PessoaFisica
from funcionario import Funcionario
from gerente import Gerente

f1 = Funcionario('Filipe', 'RM182', '123', '14/09/2001', 'Programador', 149, 'coxinha123', 5000.00)
print(f1.acessar_sistema('coxinha123'))
print(f1.calc_gratificacao())
g1 = Gerente('Filipe', 'RM182', '123', '14/09/2001', 'Programador', 149, 'coxinha123', 5000.00, 12)
print(g1.acessar_sistema('coxinha123'))
print(g1.calc_gratificacao())