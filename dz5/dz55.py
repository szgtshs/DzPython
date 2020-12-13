def summary():
    try:
        with open('dz55.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел: ')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка ввода!')


summary()
