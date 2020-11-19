# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.
def sum_of_max(a, b, c):
    x = [a, b, c]
    sum_of_two_max = []
    y = max(x)
    x.remove(y)
    sum_of_two_max.append(y)
    sum_of_two_max.append((max(x)))

    return sum(sum_of_two_max)


print(sum_of_max(40, 68, 33))
print(sum_of_max(1, 20, 8))
