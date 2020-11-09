# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
number = input("Введите число от 0 до 9 >>>")

if not number.isdigit():
    print("Неверный формат числа")
    exit()

number = int(number)
#
# if number < 0 or number > 9:
#     print("Число должно быть от 0 до 9")
# else:
#     number = number * 100 + number * 20 + number * 3
#     print(number)

chracters_count = 0
temp_number = number

while temp_number:
    temp_number //= 10
    chracters_count += 1

first_level_multiplication = (10** chracters_count) + 1
second_level_multiplication = (10** (chracters_count * 2)) + first_level_multiplication

result = number + (number * first_level_multiplication) + (number * second_level_multiplication)

print(result)
