from pessoa import Pessoa

class PessoaJuridica: 
    def __init__(self, pessoa, cnpj, data_abertura, razao_social):
        self.pessoa = pessoa
        self.cnpj = cnpj
        self.data_abertura = data_abertura
        self.razao_social = razao_social
        
    def exibir_informacoes(self):
        print(f"Nome: {self.pessoa.nome}")
        print(f"CNPJ: {self.cnpj}")
        print(f"Data abertura: {self.data_abertura}")
        print(f"Razão Social: {self.razao_social}")