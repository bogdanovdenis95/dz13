class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, цена руб. {self.price}. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            total_price_self = self.price * self.quantity
            total_price_other = other.price * other.quantity
            total_quantity = self.quantity + other.quantity
            average_price = (total_price_self + total_price_other) / total_quantity
            return Product(f"Mixed {self.name} and {other.name}", average_price, total_quantity)
        else:
            raise TypeError("Unsupported operand type(s) for +")

from product import Product

class Smartphone(Product):
    def __init__(self, name, price, quantity, performance, model, memory, color):
        super().__init__(name, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return f"{super().__str__()}, производительность: {self.performance}, модель: {self.model}, объем памяти: {self.memory}, цвет: {self.color}"

class LawnGrass(Product):
    def __init__(self, name, price, quantity, country_of_origin, germination_period, color):
        super().__init__(name, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return f"{super().__str__()}, страна производитель: {self.country_of_origin}, срок прорастания: {self.germination_period}, цвет: {self.color}"
