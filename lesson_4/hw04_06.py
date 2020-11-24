# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не
# должен быть бесконечным. Необходимо предусмотреть условие его завершения.
#
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором
# также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import count, cycle


def my_count_func(start_number, final_number):
    for x in count(start_number, 1):
        if x > final_number:
            break
        print(x, end=' ')
    print()


def my_cycle_func(list, cycle_repeat):
    for x, el in enumerate(cycle(list)):
        print(el, end=' ')
        if x >= cycle_repeat - 1:
            break


try:
    start_number = int(input("Введите начальное число для генерации целых чисел >>> "))
    final_number = int(input("Введите до какого числа включительно генерировать целые числа >>> "))
except ValueError:
    print('Нужно было внести числа')
    exit()

my_count_func(start_number, final_number)

my_list = [1, 3, 5, 8, 0]
# my_list = ["python", "java", "perl", "javascript"]
print(f'список для повторения[1, 3, 5, 8, 0]')
my_cycle_func(my_list, cycle_repeat=int(input("Cycle() Сколько раз повторить элементы списка >>> ")))
