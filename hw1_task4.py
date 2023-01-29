# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
number = int(input("Введите число:"))
max_number = 0
while number != 0:
    cur_number = number % 10 # последняя цифра = результ
    if max_number < cur_number:
        max_number = cur_number # запоминаем бОльшую
    number = number // 10 # минус одна цифра
print(max_number)
