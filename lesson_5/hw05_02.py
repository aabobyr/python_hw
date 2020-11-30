# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

data = []
with open('hw05_02_data.txt', encoding='utf-8') as my_file:
    for line in my_file.readlines():
        data.append(line.replace('\n', ''))
print(f'Количество строк в файле - {len(data)}')

for x in range(0, len(data)):
    string_list = data[int(x)].split(' ')
    print(f'Количество слов в {x + 1} строк равно {len(string_list)}')

print(data)  # проверочный принт
