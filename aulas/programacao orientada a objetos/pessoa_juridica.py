from pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, cnpj, razao_social):
        self.cnpj = cnpj
        self.razao_social = razao_social

    def validar_cnpj(self, cnpj=None):
        if cpnj is not None:
            return True
        else:
            return False
