from product import Product

class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
        else:
            raise TypeError("Only instances of Product class can be added to a category")
    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.products)} шт."
