"""еализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
методы и покажите результат."""


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'\n{self.name} поехала'

    def stop(self):
        return f'\n{self.name} остановилась'

    def turn(self, direction):
        return f'\n{self.name} повернула {direction}'

    def show_speed(self):
        return f'\n{self.speed} - скорость'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'\n{self.speed} превышение скорости'
        else:
            return f'\n{self.speed} км/ч - нормално'


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f'\n{self.speed} превышение скорости'
        else:
            return f'\n{self.speed} км/ч - нормально'


class PoliceCar(Car):
    pass


my_car = TownCar(30, 'Красненькая', 'Машинка', True)
print(my_car.go(), my_car.turn('направо'), my_car.show_speed(), my_car.stop())
