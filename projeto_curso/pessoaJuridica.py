from pessoa import Pessoa

class PessoaJuridica: 
    def __init__(self, pessoa, cnpj, data_abertura):
        self.pessoa = pessoa
        self.cnpj = cnpj
        self.data_nascimento = data_abertura
        