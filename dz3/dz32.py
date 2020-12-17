def data(name, name_2, ab, city, mail_e, tel):
    return name, name_2, ab, city, mail_e, tel


print(data(name=str(input('Введите имя: ')),
           name_2=str(input('Введите фамилию: ')),
           ab=int(input('Введите год рождения: ')),
           city=str(input('Введите город проживания: ')),
           mail_e=input('Введите e-mail: '),
           tel=int(input('Введите номер телефона: '))))
