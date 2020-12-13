# def sal():
#     try:
#         time = float(input('Выработка в часах '))
#         salary = int(input('Ставка в у.е. '))
#         bonus = int(input('Премия в у.е. '))
#         res = time * salary + bonus
#         print(f'заработная плата сотрудника  {res}')
#     except ValueError:
#         return print('Not a number')
# sal()


def salary(hours, salary_per_our, bonus):
    sal = (hours * salary_per_our) + bonus
    print(f'Зарплата - {sal}')
