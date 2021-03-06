# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число). В классе должны быть
# реализованы методы перегрузки арифметических операторов: сложение (add()),
# вычитание (sub()), умножение (mul()), деление (truediv()). Данные методы должны
# применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# целочисленное (с округлением до целого) деление клеток, соответственно.
#
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
# равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
# как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек
# между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
# то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда
# метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
# make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class Cell:
    def __init__(self, qty):
        self.qty = int(qty)

    def __str__(self):
        return f'{self.qty * "*"}'

    def __add__(self, other):
        return Cell(self.qty + other.qty)

    def __sub__(self, other):
        if (self.qty - other.qty) > 0:
            return Cell(self.qty - other.qty)
        else:
            print('Вычитание невозможно')
            return Cell(0)

    def __mul__(self, other):
        return Cell(int(self.qty * other.qty))

    def __truediv__(self, other):
        result = Cell((round(self.qty + other.qty) // 2))
        return result

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.qty / cells_in_row)):
            row += f'{"*" * cells_in_row} \n'
        row += f'{"*" * (self.qty % cells_in_row)}'
        return row


cell_1 = Cell(12)
cell_2 = Cell(15)

print(cell_1)
print(cell_2)

print()
print('Результат объединения клеток')
print(cell_1 + cell_2)
print()
print('Результат вычитания клеток cell_2 - cell_1')
print(cell_2 - cell_1)
print()
print('Результат деления клеток')
print(cell_1 / cell_2)
print()
print('Результат умножения клеток')
print(cell_1 * cell_2)
print()
print('Применение функции make_order')
print(cell_1.make_order(6))
print(cell_2.make_order(5))