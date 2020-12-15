def my_func(a, b, c):
    minimal = [a, b, c]
    minimal.remove(min(a, b, c))
    return sum(minimal)


print(my_func(6, 7, -4))
