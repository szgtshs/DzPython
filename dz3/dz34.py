# Первый вариант:
# def my_func(x, y):
#     return 1 / x ** abs(y)
#
#
# print(my_func(5, -5))


# Второй вариант:

def my_func(x, y):
    z = x
    for s in range(1, abs(y), 1):
        z = z * x
    return 1 / z


print(my_func(5, -5))
