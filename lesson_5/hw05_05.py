# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

import os
from typing import List

data = '1 21 68 9 0 12 8 7 5 13'

with open('hw05_05_source_data.txt', 'w') as data_file:  # создаем программно файл
    data_file.writelines(data)
    print(f'Cоздан файл {data_file.name}')

with open('hw05_05_source_data.txt') as my_file:
    numbers = my_file.readline().split(' ')
    print(sum(map(int, numbers)))
