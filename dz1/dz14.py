number = int(input('Введите целое положительное число: '))
num_max = 0
num = number

while num > 0:
    numeral = num % 10
    if numeral > num_max:
        num_max = numeral
    num = num // 10

print('Наибольшая цифра:', num_max)
