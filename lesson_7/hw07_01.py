# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
# принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы. Примеры матриц: см. в методичке.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде. Далее реализовать
# перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом
# сложения должна быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, first_list: list):
        self.first_list = first_list

    def __str__(self):
        output_str: str = ''
        for row in self.first_list:
            for x in row:
                output_str: str = output_str + ' ' + str(x)
            output_str += '\n'
        return output_str

    def to_list(self):
        output_list: list = []

        for row in self.first_list:
            output_row: list = []
            for x in row:
                output_row.append(x)
            output_list.append(output_row)
        return output_list

    def __add__(self, other):

        matrix_a = self.to_list()
        matrix_b = other.to_list()

        if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
            exit("Размеры матриц не совпадают, сложение матриц невозможно")

        result = []
        for row in range(len(matrix_a)):
            result_row: list = []
            for j in range(len(matrix_a[0])):
                result_row.append(0)
            result.append(result_row)

        for i in range(len(matrix_a)):
            for j in range(len(matrix_a[0])):
                result[i][j] = matrix_a[i][j] + matrix_b[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in result]))


first_matrix = Matrix([
    [31, 22, 2, 3],
    [37, 43, 4, 1],
    [51, 86, 7, 23]])

second_matrix = Matrix([
    [3, 5, 32],
    [2, 4, 6],
    [-1, 64, -8],
    [0, 4, 15]])

third_matrix = Matrix([
    [3, 5, 8, 3],
    [8, 3, 7, 1],
    [1, 1, 1, 1]])

fourth_matrix = Matrix([
    [9, 0, 2],
    [2, 6, 1],
    [1, -4, 19],
    [0, 0, 1]

])

print(f' первая матрица \n{first_matrix}')
# print(f' вторая матрица \n{second_matrix}')
print(f' третья матрица \n{third_matrix}')

print(first_matrix + third_matrix)
print()
print(second_matrix + fourth_matrix)
