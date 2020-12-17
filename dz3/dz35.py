def my_sum():
    result = 0
    ex = False
    while ex == False:
        number = input('Введите числа через пробел или q для выхода: ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q':
                ex = True
                break
            else:
                res = res + int(number[el])
        result = result + res
        print(f'Текущая сумма: {result}')
    print(f'Конечная сумма: {result}')


my_sum()
