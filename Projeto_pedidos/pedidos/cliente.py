class Cliente:
    def __init__(self, nome, sobrenome, endereco, telefone, email, genero):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.genero = genero


cliente1 = Cliente("Maria", "Joana", "123 Rua Principal", "123-456-7890", "Maria@email.com", "Feminino")
print("Nome:", cliente1.nome)
print("Sobrenome:", cliente1.sobrenome)
print("Endereço:", cliente1.endereco)
print("Telefone:", cliente1.telefone)
print("Email:", cliente1.email)
print("Gênero:", cliente1.genero)
