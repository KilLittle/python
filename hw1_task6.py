# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
revenue =  int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
if revenue >= costs:
    print("Финансовый результат - Прибыль")
    profit = (revenue - costs) / revenue
    print(f"Рентабельность {profit}")
    num_empl = int(input("Введите количество сотрудников:"))
    revenue_empl = (revenue - costs) / num_empl
    print(f"Прибыль на одного сотрудника {revenue_empl}")
else:
    print("Финансовый результат - Убыток")