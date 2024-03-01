class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, цена руб. {self.price}. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Unsupported operand type(s) for +: '{}' and '{}'".format(
                type(self).__name__, type(other).__name__))

        if type(self) != type(other):
            raise TypeError("Unsupported operand type(s) for +: '{}' and '{}'".format(
                type(self).__name__, type(other).__name__))

        total_price = self.price + other.price

        return total_price

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
