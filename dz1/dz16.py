first = float(input('Введите количество км, которые спортсмен пробежал в первый день - '))
last = float(input('Введите количество км, которое спортсмен должен пробежать - '))
day = 1
if first > last:
    print('Измените данные')
else:
    while first < last:
        first = first + (first * 0.1)
        day = day + 1
    print(f'Спортсмен пробежит за {day} дн(я, ей) {first:.1f} км')
