"""Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода
ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов
проекта, проверить на практике работу декоратора @property."""


from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def coat(self):
        pass

    @abstractmethod
    def suit(self):
        pass


class Clothes(AbstractClass):

    def __init__(self, v, h):
        self.v = v
        self.h = h

    def coat(self):
        result = round(self.v / 6.5 + 0.5, 2)
        return f'Расход ткани на пальто = {result}'

    def suit(self):
        result = round(2 * self.h + 0.3, 2)
        return f'Расход ткани на костюм = {result}'

    @property
    def total_consumption(self):
        return f'Общий расход ткани = {self.v / 6.5 + 0.5 + 2 * self.h + 0.3 :.2f}'


a = Clothes(7, 10)
print(a.coat())
print(a.suit())
print(a.total_consumption)
