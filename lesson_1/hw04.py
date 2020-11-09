# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в
# числе. Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число >>>"))

max_number = number % 10
number = number // 10

while number > 0:

    if max_number < number % 10:
        max_number = number % 10

    number = number // 10

print(f"Самое большое число {max_number}")


