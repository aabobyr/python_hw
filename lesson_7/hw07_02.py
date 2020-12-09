# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное
# название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
# одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут
# быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для
# пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на
# реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом
# уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def qty_of_cloth(self):
        pass


class Coat(Clothes):

    def __init__(self, name: str, size: float = 0):
        self.name = name
        self.size = size

    @property
    def qty_of_cloth(self):
        return f'{self.size / 6.5 + 0.5}'


class Suit(Clothes):
    def __init__(self, name: str, height: float = 0):
        self.name = name
        self.height = height

    @property
    def qty_of_cloth(self):
        return f'{self.height * 2 + 0.3}'


my_coat = Coat('пальто', 52)
your_suit = Suit('костюм', 3)

print(f'Площадь ткани на {my_coat.name} -- {my_coat.qty_of_cloth}')
print(f'Площадь ткани на {your_suit.name} -- {your_suit.qty_of_cloth}')
