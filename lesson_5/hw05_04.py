# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}
data = []
try:
    with open('hw05_04_data.txt', 'r') as my_file:
        for line in my_file:
            data_string = line.split(' - ')
            # print(data_string[0])
            if data_string[0] in dictionary:
                number = dictionary[data_string[0]]
                data.append(number + ' - ' + data_string[1])
except FileNotFoundError:
    print(f'File not found')
    exit()
try:
    with open('hw05_04_result', 'w', encoding='utf-8') as file_result:
        file_result.writelines(data)
except IOError:
    print('Some Input or Output errors')
