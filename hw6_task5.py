"""Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""


class Stationery:
    title = None

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self):
        self.title = "ручка"

    def draw(self):
        print("ручка")


class Pencil(Stationery):
    def __init__(self):
        self.title = "карандаш"

    def draw(self):
        print("карандаш")


class Handle(Stationery):
    def __init__(self):
        self.title = "маркер"

    def draw(self):
        print("маркер")


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()
