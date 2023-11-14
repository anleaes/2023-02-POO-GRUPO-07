from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, idade, cpf, data_nascimento):
        super().__init__(nome, idade)
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def exibir_informacoes(self):
        print(f"Nome: {self.pessoa.nome}")
        print(f"CPF: {self.cpf}")
