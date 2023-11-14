from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade)
        self.cpf = cpf

    def exibir_informacoes(self):
        print(f"Nome: {self.pessoa.nome}")
        print(f"CPF: {self.cpf}")
