class Category:
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._products = []

    def add_product(self, product):
        self._products.append(product)

    @property
    def products_info(self):
        info = f"Category: {self._name}\nDescription: {self._description}\nProducts:\n"
        for product in self._products:
            info += f"{product._name}, {product.price} руб. Остаток: {product.quantity} шт.\n"

        return info
