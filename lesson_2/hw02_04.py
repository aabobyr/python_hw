# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
user_input = input("Введите несколько слов через пробел >>>")

user_list = list(user_input.split())

for el in user_list:
    i = el
    if len(i) > 10: i = i[:10]
    print(f" {i} -- длина {len(i)}")
