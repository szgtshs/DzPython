lost = float(input('Введите издержки:'))
profit = float(input('Введите выручку:'))

total = profit - lost

if total > 0:
        print('Финансовый результат:', total)
        staff = int(input('Введите количество сотрудников:'))
        if staff > 0:
            total_staff = total / staff
            print(f'Прибыль фирмы в расчете на одного сотрудника: {total_staff:.2f}')
else:
    print('Фирма работает в убыток')