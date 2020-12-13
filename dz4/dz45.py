from functools import reduce


def my_work(num_p, num):
    return num_p * num


print(f'Список четных значений:\n{[num for num in range(99, 1001) if num % 2 == 0]}')
print(f'Результат перемножения всех элементов:\n{reduce(my_work, [num for num in range(99, 1001) if num % 2 == 0])}')
