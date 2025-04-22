# Домашняя работа 14.1

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
from src.classes import Product, Category

# Пример создания объекта класса Product
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

# Пример создания объекта класса Category
category = Category("Смартфоны",
"Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
[product1, product2, product3])
```