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
obra1.exibir_informacoes()
