from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    @property
    def calculate(self):
        return f'Для пошива пальто нужно - {round((self.param / 6.5) + 0.5):.2f} ткани'


class Suit(Clothes):

    @property
    def calculate(self):
        return f'Для пошива костюма нужно - {round((2 * self.param) + 0.3):.2f} ткани'


coat = Coat(45)
suit = Suit(170)
print(coat.calculate)
print(suit.calculate)
