# Домашняя работа 16.1

## Описание:

В данном проекте я реализовываю ядро для интернет-магазина.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/username/project.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```

3. Создайте базу данных и выполните миграции:
```
python manage.py migrate
```

4. Запустите локальный сервер:
```
python manage.py runserver
```
## Использование:
```python
from src.classes import *

# Пример создания объекта класса Product
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

#Пример создания товаров по категориям
smartphone = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

# Пример создания объекта класса Category
category = Category("Смартфоны",
"Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
[product1, product2, product3])

# Пример использования add_product
product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
category.add_product = product4

# Пример использования new_product
new_product = Product.new_product({"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,"quantity": 5})
```
