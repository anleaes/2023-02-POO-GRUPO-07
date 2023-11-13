class PessoaFisica:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Data de Nascimento: {self.data_nascimento}")


pessoa = PessoaFisica("João da Silva", "123.456.789-00", "01/01/1980")
print("Nome:", pessoa.nome)
print("CPF:", pessoa.cpf)
print("Data de nascimento:", pessoa.data_nascimento)