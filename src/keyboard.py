from src.item import Item


class LangKeyBoard:
    """
    - Реализуйте дополнительный функционал по хранению и изменению раскладки клавиатуры в отдельном классе-миксине, который “подмешивается” в цепочку наследования класса `Keyboard`.
    """

    def __init__(self, name, price, quantity):
        self.__language = "EN"
        super().__init__(name, price, quantity)

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
            return self
        else:
            self.__language = "EN"
            return self


class KeyBoard(LangKeyBoard, Item):
    """
    - Создайте класс `Keyboard` для товара “клавиатура”.

> Товар отличается от `Item` тем, что у него есть атрибут `language` и метод для изменения языка (раскладки клавиатуры).
> Язык по умолчанию (при инициализации) - английский (`EN`). Всего поддерживается два языка: `EN` и `RU`.
> Изменить язык можно только методом `change_lang()
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        KeyBoard.all.append(self)
