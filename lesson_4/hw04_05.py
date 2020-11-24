# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
# четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов
# списка. Подсказка: использовать функцию reduce().
from functools import reduce

min_value = 100
max_value = 1000

result_list = [x for x in range(min_value, max_value + 1) if x % 2 == 0]

total = reduce(lambda total, amount: total * amount, result_list)

print(result_list)
print(total)



