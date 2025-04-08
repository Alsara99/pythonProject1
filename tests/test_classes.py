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
    assert len(category.products) == 3