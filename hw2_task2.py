# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().
my_list = input("Введите числа через ,: ").split(',')
i_even, j_odd = 0, 1
while len(my_list) > j_odd:
    my_list[i_even], my_list[j_odd] = my_list[j_odd], my_list[i_even]
    i_even += 2
    j_odd += 2
print(*my_list)