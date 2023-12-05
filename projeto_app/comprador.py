class comprador:
    def __init__(self, nome, cpf, historico_compras=[]):
        self.nome = nome
        self.cpf = cpf
        self.historico_compras = historico_compras

    def adicionar_compra(self, obra_de_arte):
        self.historico_compras.append(obra_de_arte)
        print(f"Compra realizada com sucesso por {self.nome}!")

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print("Histórico de Compras:")
        for obra in self.historico_compras:
            print(f"- {obra.titulo} de {obra.artista} ({obra.ano})")


comprador1 = comprador("João", "034.636.731-43")
comprador2 = comprador("Maria", "321.412.231-10")
comprador3 = comprador("José", "321.444.555-01")

#comprador1.exibir_informacoes()
