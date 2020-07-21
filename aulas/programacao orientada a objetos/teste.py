from classes import soma
from carro import Carro

print(soma(1,2))

carro1 = Carro(1.5, 'hidraulica', True, 'Volkswagen')
print(carro1.motor)
print(carro1.eletrico)
print(carro1.partida())
print(carro1.acelera())
print(carro1.parar())