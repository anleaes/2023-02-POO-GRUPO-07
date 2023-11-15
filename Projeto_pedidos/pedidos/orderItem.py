from order import Order
from product import Product

class OrderItem:
    def __init__(self, quantity, unitary_price, order, product):
        self.quantity = quantity
        self.unitary_price = unitary_price
        self.order = order
        self.product = product