class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    def __str__(self):
        return f"{self._name}, {self._price} руб. Остаток: {self._quantity} шт."

    def __add__(self, other):
        total_price_self = self._price * self._quantity
        total_price_other = other._price * other._quantity
        return total_price_self + total_price_other