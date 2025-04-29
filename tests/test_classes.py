from logging import exception

import pytest
from src.classes import *


@pytest.fixture
def samsung_product():
    return Product("Samsung Galaxy S23 Ultra",
                   "256GB, Серый цвет, 200MP камера",
                   180000.0,
                   5)


@pytest.fixture
def samsung_product1():
    return Product("Samsung Galaxy S24 Ultra",
                   "256GB, Серый цвет, 200MP камера",
                   250000.0,
                   7)


@pytest.fixture
def grass1():
    return LawnGrass("Газонная трава",
                 "Элитная трава для газона",
                      500.0, 20,
                    "Россия",
            "7 дней", "Зеленый")


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


def test_str_output(samsung_product):
    assert str(samsung_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add(samsung_product, samsung_product1):
    assert samsung_product + samsung_product1


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


def test_str(category):
    assert str(category) == "Смартфоны, количество продуктов: 27 шт."


def test_sum_different_products(samsung_product, grass1):
    try:
        samsung_product + grass1
    except Exception as e:
        assert type(e) == type(TypeError())


def test_add_none_product(category):
    try:
        category.add_product = "Not a product"
    except Exception as e:
        assert type(e) == type(TypeError())
