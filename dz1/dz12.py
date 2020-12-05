clock = int(input('Введите количество секунд '))
hours = clock // 3600
minutes = (clock // 60) - (hours * 60)
seconds = clock % 60
print(f'Время - чч:мм:сс - {hours} : {minutes} : {seconds}')
