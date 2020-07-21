from funcionario import Funcionario

class Gerente(Funcionario):
    
    def __init__(self, nome, end, cpf, dt_nasc, cargo, matricula, senha, salario, qtd_funcionario):
        super().__init__(nome, end, cpf, dt_nasc, cargo, matricula, senha, salario)
        self._qtd_funcionario = qtd_funcionario

    def calc_gratificacao(self):
        return self._salario * 0.15