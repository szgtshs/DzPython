def delenie():
    try:
        del_1 = int(input('Введите делимое: '))
        del_2 = int(input('Введите делитель: '))
        result = del_1 / del_2
    except ValueError:
        return 'Число не введено!'
    except ZeroDivisionError:
        return 'Делить на 0 нельзя!'
    return result


print('Равно:', delenie())
