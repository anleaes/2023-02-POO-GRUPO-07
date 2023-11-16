from pessoa import Pessoa

class PessoaFisica:
    def __init__(self, pessoa, cpf, data_nascimento ):
        self.pessoa = pessoa
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def exibir_informacoes(self):
        print(f"Nome: {self.pessoa.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Data de nascimento: {self.data_nascimento}")
