from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, endereco, cpf, dt_nasc):
        super().__init__(nome, endereco)
        self.cpf = cpf
        self.dt_nasc = dt_nasc

    def validar_cpf(self, cpf):
        if cpf is not None:
            return True
        else:
            return False