import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    def __init__(self, name:str, price:float, quantity:int) -> None:
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

    @staticmethod
    def instantiate_from_csv():
        """ класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv"""
        with open('../src/items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                Item(i["name"], int(i["price"]), int(i["quantity"]))
    @staticmethod
    def string_to_number(string: str):
        """статический метод, возвращающий число из числа-строки"""
        float_str = float(string)
        return int(float_str)

