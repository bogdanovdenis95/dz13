from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    @abstractmethod
    def create_product(self, name, description, price, quantity):
        pass

class Product(AbstractProduct):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', description='{self.description}', price={self.price}, quantity={self.quantity})"


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return f"{self.name}, цена: {self.price}, описание: {self.description}"

    def calculate_total_price(self):
        return self.price * self.quantity

    def create_product(self, name, description, price, quantity):
        return self.__class__(name, description, price, quantity, self.performance, self.model, self.memory, self.color)


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country_of_origin, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return f"{self.name}, цена: {self.price}, описание: {self.description}"

    def calculate_total_price(self):
        return self.price * self.quantity

    def create_product(self, name, description, price, quantity):
        return self.__class__(name, description, price, quantity, self.country_of_origin, self.germination_period, self.color)
