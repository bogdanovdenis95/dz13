class Category:
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._products = []

    def __str__(self):
        return f"{self._name}, количество продуктов: {len(self._products)} шт."

    def add_product(self, product):
        self._products.append(product)