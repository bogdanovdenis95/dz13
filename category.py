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
        if product.quantity == 0:
            raise ValueError("Cannot add a product with zero quantity.")
        self.products.append(product)

    def calculate_average_price(self):
        if not self.products:
            return 0
        total_price = sum(product.price for product in self.products)
        return total_price / len(self.products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.products)} шт."

    def calculate_average_price(self):
        try:
            total_price = sum(product.price for product in self.products)
            return total_price / len(self.products)
        except ZeroDivisionError:
            return 0

