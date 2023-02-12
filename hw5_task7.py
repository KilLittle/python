"""Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные
о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста."""


import json
profit = {}
intermed_profit = {}
prof = 0
average_profit = 0
i = 0
with open('test.txt', 'r', encoding='utf_8') as my_file:
    for line in my_file:
        name_firm, form, income, expenses = line.split()
        profit[name_firm] = int(income) - int(expenses)
        if profit.setdefault(name_firm) >= 0:
            prof = prof + profit.setdefault(name_firm)
            i += 1
    if i != 0:
        average_profit = prof / i
        print(f'Средняя прибыль:  {average_profit:.2f}')
    else:
        print(f'Прибыли нет')

with open('result.json', 'w') as write_js:
    json.dump(profit, write_js)
    js_str = json.dumps(profit)
    print(js_str)
