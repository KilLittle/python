""" Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой."""


def func_data(name, lastname, year_birth, city, email, phone):
    return print(f'Имя: {name} Фамилия: {lastname} Год рождения: {year_birth}'
                 f'Город проживания: {city} Email: {email} Телефон: {phone}')


func_data(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    year_birth=input('Год рождения: '),
    city=input('Город проживания: '),
    phone=input('phone: '),
    email=input('email: '),
)
