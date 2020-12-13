from itertools import count
from math import factorial


def fibo_gen():
    for el in count(1):
        yield factorial(el)


gen = fibo_gen()
x = 1
for n in gen:
    if x < 16:
        print(f'Факториал - {x}: ', n)
        x += 1
    else:
        break
