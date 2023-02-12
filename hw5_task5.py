"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран."""


with open('New_test.txt', 'w+') as file_obj:
    line = input('Введите числа через пробел: ')
    file_obj.writelines(line)
    my_numb = line.split()

print(sum(map(int, my_numb)))
