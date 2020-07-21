class Carro:
    def __init__(self, motor, direcao, eletrico, marca):
        print('Construtor chamado')
        print('self: {}'.format(self)),

        self.motor = motor
        self.direcao = direcao
        self.eletrico = eletrico
        self.marca = marca
        
    def partida(self):
        print('Dando partida...')

    def acelera(self):
        print('Acelerando...')
    
    def parar(self):
        print('Carro parado.')