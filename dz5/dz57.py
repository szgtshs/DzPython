import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('dz57.txt', encoding='utf-8') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'Средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании:\n{profit}')

with open('dz571.json', 'w') as write_js:
    json.dump(profit, write_js)

with open('dz571.json', encoding='utf-8') as write_js:
    print(f'Создан файл с расширением json:\n{json.load(write_js)}')
