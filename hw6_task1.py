"""Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) —
на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
завершать скрипт."""

import time


class TrafficLight:
    red_time = 7
    yellow_time = 2
    green_time = 9

    def __init__(self, color):
        self._color = color

    def switch_color(self, color, color_time):
        self.color_time = color_time
        print(f'{color} свет.')
        time.sleep(self.color_time)

    def running(self):
        self.switch_color('красный', self.red_time)
        self.switch_color('желтый', self.yellow_time)
        self.switch_color('зеленый', self.green_time)


a = TrafficLight('красный')
a.running()
