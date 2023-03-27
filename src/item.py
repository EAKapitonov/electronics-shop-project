import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        """
         - реализуйте возможность сложения экземпляров класса `Phone` и `Item` (сложение по количеству товара в магазине)
         - Реализуйте проверки, чтобы нельзя было сложить `Phone` или `Item` с экземплярами не `Phone` или `Item` классов.
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if len(name) < 11:
            self.__name = name
        else:
            return "Длина наименования товара превышает 10 символов"

    @classmethod
    def instantiate_from_csv(cls, url_file='../src/items.csv'):
        """ класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv"""
        with open(url_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                Item(i["name"], int(i["price"]), int(i["quantity"]))

    @staticmethod
    def string_to_number(string: str):
        """статический метод, возвращающий число из числа-строки"""
        float_str = float(string)
        return int(float_str)
