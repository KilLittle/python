"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def calculator(arg_1, arg_2):
    try:
        return arg_1 / arg_2
    except ZeroDivisionError:
        return 'Деление на ноль!'


arg_1 = int(input('Первое число: '))
arg_2 = int(input('Второе число: '))
print(calculator(arg_1, arg_2))
