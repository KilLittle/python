"""Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух
аргументов."""


def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    my_list.sort()  # отсортировать
    sum_max = my_list[1] + my_list[2]  # складываем два последних
    print(f'Сумма двух наибольших: {sum_max}')


my_func(
    arg_1=int(input('Число 1: ')),
    arg_2=int(input('Число 2: ')),
    arg_3=int(input('Число 3: '))
)
