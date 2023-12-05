class ObraDeArte:
    def __init__(self, titulo, artista, ano, valor):
        self.titulo = titulo
        self.artista = artista
        self.ano = ano
        self.valor = valor

    def exibir_informacoes(self):
        print(f"Obra: {self.titulo}")
        print(f"Artista: {self.artista}")
        print(f"Ano: {self.ano}")
        print(f"Valor: {self.valor}")


obra1 = ObraDeArte("A Noite Estrelada", "Vincent van Gogh", 1889, "inegociavel")
obra2 = ObraDeArte("Mona Lisa", "Leonardo da Vinci", 1517, "inegociavel")
obra3 = ObraDeArte("Les Femmes d'Alger ", "Pablo Picasso", 1955, "US$ 179,4 milhões")

#talvez seja mais interessante colocar na main igual o outro projeto
#obra1.exibir_informacoes()
#obra2.exibir_informacoes()
#obra3.exibir_informacoes()