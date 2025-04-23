import pytest
from src.classes import *


@pytest.fixture
def samsung_product():
    return Product("Samsung Galaxy S23 Ultra",
                   "256GB, Серый цвет, 200MP камера",
                   180000.0,
                   5)


def test_init(samsung_product):
    assert samsung_product.name == 'Samsung Galaxy S23 Ultra'
    assert samsung_product.description == '256GB, Серый цвет, 200MP камера'
    assert samsung_product.price == 180000.0
    assert samsung_product.quantity == 5


def test_price(samsung_product):
    new_value = 16000
    samsung_product.price = new_value
    assert samsung_product.price == new_value


def test_price_exception(samsung_product):
    try:
        new_value = 0
        samsung_product.price = new_value
    except ValueError as error:
        assert str(error) == "Ошибка"


@pytest.fixture
def category():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category("Смартфоны",
                "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                [product1, product2, product3])


def test_init_category(category):
    assert category.name == 'Смартфоны'
    assert category.description == 'Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни'


def test_category_count(category):
    assert category.category_count == 2


def test_product_count(category):
    assert category.product_count == 3


def test_new_product(samsung_product):
    new_product = Product.new_product({"name": "Samsung Galaxy S23 Ultra",
    "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,"quantity": 5})
    assert type(new_product) == type(samsung_product)


def test_add_product(category):
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category.add_product = product4
    assert category.category_count == 4
    assert category.product_count == 4
