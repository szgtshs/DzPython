class Car:

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехал(а).'

    def stop(self):
        return f'\nМашина {self.name} остановилась'

    def turn(self, direction):
        return f'\nМашина {self.name} повернул(а) {direction}'

    def show_speed(self):
        return f'Скорость машины: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Внимание! Превышение скорости! Ваша скорость: {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Внимание! Превышение скорости! Ваша скорость: {self.speed}'


class PoliceCar(Car):
    pass


town = TownCar('Форд', 67, 'белый', False)
print('1:' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar('БМВ', 156, 'черный', False)
print('2:' + sport.go(), sport.show_speed(), sport.turn('направо'), sport.stop())

work = WorkCar('Камаз', 30, 'оранжевый', False)
print('3:' + work.go(), work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar('Лада', 100, 'голубой', True)
print('4:' + work.go(), work.show_speed(), work.turn('налево'), work.stop())
