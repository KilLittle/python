# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.
my_list = input("Введите слова через пробел: ").split()
n = 1
for el in my_list:
    if len(el) > 10:
        print(f"{n}) {el[:10]}")
    else:
        print(f"{n}) {el}")
    n += 1
print()
