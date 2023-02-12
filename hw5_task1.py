"""Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка."""

my_file = open('test.txt', 'w', encoding="utf-8")
while True:
    input_text = input('Введите текст в строку: \n')
    my_file.writelines(f"{input_text}\n")
    if not input_text:
        break
my_file.close()
