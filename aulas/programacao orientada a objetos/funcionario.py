from pessoa_fisica import PessoaFisica

class Funcionario(PessoaFisica):
    def __init__(self, nome, end, cpf, dt_nasc, cargo, matricula, senha, salario):
        super().__init__(nome, end, cpf, dt_nasc)
        self._cargo = cargo
        self._matricula = matricula
        self._senha = senha
        self._salario = salario
    def acessar_sistema(self, senha):
        if self._senha == senha:
            return True
        else:
            return False

    def calc_gratificacao(self):
        return self._salario * 0.10
