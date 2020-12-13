with open('dz51.txt', 'w') as file:
    while True:
        line = input('Введите текст: ')
        if line == '':
            break
        file.write(line + '\n')
