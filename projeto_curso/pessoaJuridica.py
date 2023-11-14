from pessoa import Pessoa

class Pessoa_Juridica(Pessoa): 
    
    def __init__(self, nome, endereco, cnpj, data_abertura):
        super().__init__(nome, endereco)
        self.cnpj = cnpj
        self.data_nascimento = data_abertura
        