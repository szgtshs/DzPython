from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = ('Красный', 'Желтый', 'Зеленый')

    def running(self):
        c = 0
        while c != 3:
            print(self.__color[c])
            if c == 0:
                sleep(7)
            elif c == 1:
                sleep(2)
            elif c == 2:
                sleep(5)
            c += 1


lights = TrafficLight()
lights.running()
