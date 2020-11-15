# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# try:
#     number_of_list_elements = int(input("введите количество элементов"))
# except ValueError:
#     print("Нужно было ввести число")
#     exit()
# while number_of_list_elements > 0:
#     element_list += input("Введите элемент списка")
#     number_of_list_elements -= 1

element_list = list(input("Введите элементы списка, без разделителей, одна цифра один элемент>>>"))

print(f'Исходный список - {element_list}')

a = len(element_list)
count = 0
a = a if 0 == (a % 2) else a - 1

while count < a:
    element_list[count], element_list[count + 1] = element_list[count + 1], element_list[count]
    count += 2
print(f'Список после перестановки элементов - {element_list}')
