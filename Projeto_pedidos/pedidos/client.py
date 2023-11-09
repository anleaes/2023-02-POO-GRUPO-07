class Client:
    def __init__(self, first_name, last_name, address, cell_phone, email, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.cell_phone = cell_phone
        self.email = email
        self.gender = gender

# Exemplo de uso da classe Client
client1 = Client("João", "Silva", "123 Rua Principal", "123-456-7890", "joao@email.com", "Masculino")
print("First Name:", client1.first_name)
print("Last Name:", client1.last_name)
print("Address:", client1.address)
print("Cell Phone:", client1.cell_phone)
print("Email:", client1.email)
print("Gender:", client1.gender)