from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, endereco, cpf, data_nascimento ):
        super().__init__(nome, endereco)
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def exibir_informacoes(self):
        print(f"Nome: {self.pessoa.nome}")
        print(f"CPF: {self.cpf}")
