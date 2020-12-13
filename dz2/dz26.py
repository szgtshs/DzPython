num = 0
analysis = {'Наименование товара': [], 'Цена товара': [], 'Количество': [], 'Единица измерения': []}
while True:
    if input('Для аналитики товара введите - y: ') == 'y':
        num += 1
        name = input('Наименование товара: ')
        price = int(input('Цена товара: '))
        number = int(input('Количество: '))
        unit = input('Единица измерения: ')
        products = {'Наименование товара': name, 'Цена товара': price, 'Количество': number, 'Единица измерения': unit}
        for k in products.keys():
            analysis[k].append(products[k])
            products = products.copy()
        print('Текущая аналитика: ', num, analysis)
        continue
    for key, values in analysis.items():
        print(key, values)
    break
