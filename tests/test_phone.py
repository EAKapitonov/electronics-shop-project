from src.phone import Phone
from src.item import Item

import pytest


@pytest.fixture
def name():
    return "iphone 14pro"


@pytest.fixture
def price():
    return 120000.0


@pytest.fixture
def quantity():
    return 10


@pytest.fixture
def number_of_sim():
    return 2


def test_Phone(name, price, quantity, number_of_sim):
    product = Phone(name, price, quantity, number_of_sim)
    Phone.pay_rate = 0.85
    assert product.name == "iphone 14pro"
    assert product.price == 120000.0
    assert product.calculate_total_price() == 1200000.0
    product.apply_discount()
    assert product.price == 102000


def test_name():
    """тестируем name сеттер"""
    assert Phone.all[0].name == "iphone 14pro"
    Phone.all[0].name = "Телефон"
    assert Phone.all[0].name == "Телефон"


def test_str():
    """тестируем __str__"""
    assert repr(Phone.all[0]) == "Phone('Телефон', 102000.0, 10, 2)"
    assert str(Phone.all[0]) == 'Телефон'


def test_add():
    """
    тестируем сложение обьектов
    """
    assert Item.all[1] + Phone.all[0] == 11
    assert Phone.all[0] + Phone.all[0] == 20
