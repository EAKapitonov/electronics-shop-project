from src.item import Item, InstantiateCSVError
import pytest
"""Здесь надо написать тесты с использованием pytest для модуля item."""
@pytest.fixture
def name():
    return "iphone 5S"
@pytest.fixture
def price():
    return 20000.0
@pytest.fixture
def quantity():
    return 15

def test_Item(name, price, quantity):
    product = Item(name, price, quantity)
    Item.pay_rate = 0.85
    assert product.name == "iphone 5S"
    assert product.price == 20000.0
    assert product.calculate_total_price() == 300000
    product.apply_discount()
    assert product.price == 17000

def test_instantiate_from_csv():
    """тестируем instantiate_from_csv()"""
    Item.instantiate_from_csv("src/items.csv")
    assert Item.all[1].price == 100
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("src/items2.csv")
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("src/items3.csv")
    assert Item.instantiate_from_csv("src/items4.csv") == "не допустимое значение параметров товара"
    assert Item.instantiate_from_csv("src/items5.csv") == "_Отсутствует файл item.csv_"


def test_name():
    """тестируем name сеттер"""
    assert Item.all[1].name == "Смартфон"
    Item.all[1].name = "Телефон"
    assert Item.all[1].name == "Телефон"

def test_string_to_number():
    """тестируем string_to_number()"""
    assert Item.string_to_number('7') == 7
    assert Item.string_to_number('7.2') == 7
    assert Item.string_to_number('8.87') == 8


def test_str():
    """тестируем __str__"""
    assert repr(Item.all[1]) == "Item('Телефон', 100, 1)"
    assert str(Item.all[1]) == 'Телефон'
