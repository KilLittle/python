# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
input_a = int(input("Введите результат в первый день а ="))
input_b = int(input("Введите результат b ="))
num_days = 1
while input_a < input_b:
    num_days += 1
    input_a = input_a + input_a * 0.1
print(num_days)