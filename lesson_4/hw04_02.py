# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента. Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка
# использовать генератор. Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]. Результат: [12,
# 44, 4, 10, 78, 123].

source_list = [300.1, 300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 58, 0, 66, 7, 21, 1, 0.33, 0.72]

result_list = [source_list[x] for x in range(1, len(source_list)) if source_list[x] > source_list[x - 1]]

print(result_list)
# Некорректно, в таком варианте при первом проходе сравнивает нулевой элемент с финальным элементом списка
# result_list_1 = [x for x in source_list if x > source_list[source_list.index(x) - 1]]
# print(source_list[0 - 1])
# print(f'ошибочный {result_list_1}')
