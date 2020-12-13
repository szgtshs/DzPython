class Worker:

    def __init__(self, name='', surname='', position='', wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


w_man = Position('Ivan', 'Ivanov', 'taxi driver', 150, 50)
print(f'Данные: {w_man.name}, {w_man.surname}, {w_man.position}, {w_man._income}')
print(f'Доход {w_man.get_full_name()} составляет - {w_man.get_total_income()}')
