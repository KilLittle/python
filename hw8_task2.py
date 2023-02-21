"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой."""


class MyDivision:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def fun_division(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Делать на ноль нельзя")


div = MyDivision(10, 100)
print(div.fun_division(100, 0))
