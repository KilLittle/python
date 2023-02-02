""" Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
ранее сумме и после этого завершить программу."""


def calc_sum(string):
    my_list = string.split(" ")
    mas = []
    try:
        for el in my_list:
            mas.append(int(el))
    except ValueError:
        return sum(mas)
    return sum(mas)


fin_sum = 0
int_number = ''
while int_number != '-':
    int_number = input('Введите целое число через пробел или "-" для выхода: ')
    sum_num = calc_sum(int_number)
    fin_sum += sum_num
    print(f'Сумма = {fin_sum}')
