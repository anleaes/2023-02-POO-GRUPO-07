class Pessoa_Juridica: 
    
    def __int__(self, nome_empresa, cnpj):
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj
        
    def exibir_info(self):
        print(f"Nome da empresa: {self.nome_empresa}")
        print(f"CNPJ: {self.cnpj}")
