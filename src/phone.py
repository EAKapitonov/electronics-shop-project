from src.item import Item


class Phone(Item):
    """
         > `Phone` содержит все атрибуты класса `Item` и дополнительно атрибут, содержащий количество поддерживаемых сим-карт
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int, count_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = count_sim
        Phone.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
