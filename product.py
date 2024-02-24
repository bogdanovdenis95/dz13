class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be non-negative")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity must be non-negative")
        self._quantity = value

    def __str__(self):
        return f"{self._name}, {self._price} руб. Остаток: {self._quantity} шт."

    def __add__(self, other):
        total_price_self = self._price * self._quantity
        total_price_other = other._price * other._quantity
        total_quantity = self._quantity + other._quantity
        new_price = (total_price_self + total_price_other) / total_quantity
        return Product("Merged Product", new_price, total_quantity)