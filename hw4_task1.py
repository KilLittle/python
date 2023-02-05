""" Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. Используйте
в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений
необходимо запускать скрипт с параметрами."""

from sys import argv

f_obj, name_v, hours_v, rate_v = argv
print(f_obj)



def calc_salary(hours, rate):
    try:
        print(f"Сотрудник {name_v} заработал {(int(hours) * int(rate)) * 2}")
    except TypeError:
        print("Неверное значение")
        exit()


calc_salary(hours_v, rate_v)

