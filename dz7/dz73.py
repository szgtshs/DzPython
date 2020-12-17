class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Объединение двух клеток. Размер клетки - {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Клетка стала меньше. Размер клетки - {sub}' if sub > 0 else 'Клетка исчезла :('

    def __truediv__(self, other):
        return f'Делится общая клетка из двух. Размер клетки - {self.quantity // other.quantity}'

    def __mul__(self, other):
        return f'Множится общая клетка из двух. Размер клетки - {self.quantity * other.quantity}'

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell = Cell(70)
cell_2 = Cell(7)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(7))
