from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        super().__init__()
        pass


class MixinLog:
    def __init__(self, *args, **kwargs):
        print(f"({self.__class__.__name__}, {', '.join(repr(arg) for arg in self.__dict__.values())})")


    def __repr__(self):
        return f"({self.__class__.__name__}, {', '.join(repr(arg) for arg in self.__dict__.values())})"


class Product(BaseProduct, MixinLog):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)


    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."


    def __add__(self, other):
        if isinstance(self, type(other)):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, new_value):
        if new_value > 0:
            self.__price = new_value
        else:
            print("Цена не должна быть нулевая или отрицательная")
            raise ValueError("Ошибка")


    @classmethod
    def new_product(cls, dictionary):
        name, description, price, quantity = dictionary.values()
        return cls(name, description, price, quantity)


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count = len(products)


    def __str__(self):
        count = 0
        for i in self.__products:
            count += i.quantity
        return f"{self.name}, количество продуктов: {count} шт."


    @property
    def products(self):
        result = ''
        for i in self.__products:
            result = result + f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.\n"
        return result

    @products.setter
    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError
