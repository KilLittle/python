"""Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1
см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т."""

class Road():
    length = 0
    width = 0

    def __init__(self, length, width, weight, depth):
        self.length = length
        self.width = width
        self.weight = weight
        self.depth = depth

    def total(self):
        new_total = self.length * self.width * self.weight * self.depth / 1000
        return new_total

a = Road(200, 50, 25, 0.1)
print(f'Масса асфальта {a.total()} тонн')