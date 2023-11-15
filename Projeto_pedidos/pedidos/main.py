from category import Category
from product import Product
from client import Client
from socialNetwork import Socialnetwork
from orderItem import OrderItem
from order import Order
from clientSocialNetwork import ClientSocialnetwork


categoria = Category(1, 'roupas', 'descrição da categoria')
produto = Product('regata', 'regata branca','10/10/2024', 'ativo', categoria)
cliente = Client('Andrew', 'Sobrera', 'Rua tupi','(51)99999-9999', 'teste@teste.com', 'masculino')
socialnetwork = Socialnetwork('Instagram', 'rede social')

pedido = Order(40.00, 'separado', cliente)
orderItem = OrderItem(2, 20.00, pedido, produto)
cliente_rede_social = ClientSocialnetwork(cliente, socialnetwork)

print("Produto: ", produto.name)
print("Valor total do pedido: ", pedido.total_price)
print("Nome do Cliente: ", cliente.first_name, cliente.last_name)
print("Rede social do cliente:", cliente_rede_social.socialnetwork.name)