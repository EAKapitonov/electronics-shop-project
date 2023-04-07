from src.item import Item
"""
"../src/items.csv" - нормальный файл
"../src/items2.csv" - файл без 1 одного столбика
"../src/items3.csv" - файл без значения 1 товара
"../src/items4.csv" - файл с неподходящим значением в 1 товаре
"../src/items4.csv" - файл отсутсвует

Для проверки меняйте ссылки передаваемуюы в функцию 

"""
if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv("../src/items4.csv")
    # FileNotFoundError: Отсутствует файл item.csv
    # В файле items.csv удалена последняя колонка.
    # InstantiateCSVError: Файл item.csv поврежден
