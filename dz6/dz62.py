class Road:
    def __init__(self, length, width, thickness, mass):
        self._leghth = length
        self._width = width
        self._thickness = thickness
        self._mass = mass

    def end_mass(self):
        all_mass = self._leghth * self._width * self._mass * (self._thickness / 1000)
        return all_mass


my_road = Road(100, 10000, 4, 30)
print('Потребуется: ', my_road.end_mass(), 'тонн(ы)')
