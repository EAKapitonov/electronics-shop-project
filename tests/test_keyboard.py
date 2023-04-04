from src.keyboard import KeyBoard
import pytest


@pytest.fixture
def kb():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    return kb


def test_keyboard(kb):
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"


def test_change_lang(kb):
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"
