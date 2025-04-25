class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."


    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity


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
        self.__products.append(product)
        Category.product_count += 1
