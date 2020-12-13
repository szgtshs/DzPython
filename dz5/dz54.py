with open('dz54.txt', encoding='utf-8') as f:
    lines = f.readlines()

translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
dz541 = []
with open('dz54.txt', 'r', encoding='utf-8') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        dz541.append(translate[i[0]] + ' ' + i[1])

with open('dz541.txt', 'w', encoding='utf-8') as file_obj_2:
    file_obj_2.writelines(dz541)
