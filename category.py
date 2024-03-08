from product import Product

class LoggingMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект: {self.__repr__()}")


class Category(LoggingMixin):
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
        self.products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Only instances of Product class can be added to the category.")
        self.products.append(product)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.products)} шт."
