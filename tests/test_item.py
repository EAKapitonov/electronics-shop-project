from src.item import Item
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
    Item.instantiate_from_csv()
    assert Item.all[1].price == 100

def test_string_to_number():
    """тестируем string_to_number()"""
    assert Item.string_to_number('7') == 7
    assert Item.string_to_number('7.2') == 7
    assert Item.string_to_number('8.87') == 8

def test_name():
    """тестируем name сеттер"""
    assert Item.all[1].name == "Смартфон"
    Item.all[1].name = "Телефон"
    assert Item.all[1].name == "Телефон"