# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
# одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    expence_count = 0

    @abstractmethod
    def expence(self):
        pass


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        Suit.expence_count += self.expence

    def __str__(self):
        return f' Размер костюма: {self.height}, расход ткани: {self.expence}, общий расход ткани: {Suit.expence_count:.02f}'

    @property
    def  expence(self):
        exp = self.height * 2 + 0.3
        return float(f'{exp:.02f}')

class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.expence_count += self.expence

    def __str__(self):
        return f' Размер пальто: {self.size}, расход ткани: {self.expence}, общий расход ткани: {Coat.expence_count:.02f}'

    @property
    def expence(self):
        exp = self.size / 6.5 + 0.5
        return float(f'{exp:.02f}')


cloth_1 = Suit(115)
print(cloth_1)
cloth_2 = Suit(150)
print(cloth_2)
cloth_3 = Coat(170)
print(cloth_3)
cloth_4 = Coat(150)
print(cloth_4)


