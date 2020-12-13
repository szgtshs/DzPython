# from itertools import count
#
#
# for num in count(int(input('Введите стартовое число '))):
#     print(num)
#

from itertools import cycle

my_list = [True, 'ABC', 123, None]
for num in cycle(my_list):
    print(num)
