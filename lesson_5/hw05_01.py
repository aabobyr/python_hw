# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных свидетельствует пустая строка.

user_info = []
while True:
    user_input = input(f"Введите данные. для окончания ввода введите пустую строк >>>")
    if user_input == '':
        break
    else:
        user_info.append(user_input)

with open('user_data.txt', 'w', encoding='utf-8') as printable:
    for x in user_info:
        print(x, file=printable)
print('данные записаны в файл')
