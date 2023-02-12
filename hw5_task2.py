"""Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой
строке."""

my_file = open('test.txt', 'r', encoding='utf-8')
line_text = my_file.readlines()
print(f'Строк в файле: {len(line_text)}')
my_cnt = 0
for line in line_text:
    my_cnt += 1
    result_line = line.split()
    print(f'{my_cnt} строка {len(result_line)} слов')
