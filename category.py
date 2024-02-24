class Category:
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._products = []

    def add_product(self, product):
        self._products.append(product)

    @property
    def products_info(self):
        info = f"{self._name}, количество продуктов: {len(self._products)} шт."
        return info

    def __str__(self):
        return self.products_info
