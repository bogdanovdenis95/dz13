from product import AbstractProduct

class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []

    def add_product(self, product):
        if not isinstance(product, AbstractProduct):
            raise TypeError("Only instances of AbstractProduct class can be added to the category.")
        self.products.append(product)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.products)} шт."
