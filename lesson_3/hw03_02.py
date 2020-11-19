# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(name, surname, birthyear, city, email, phone):
    print(name, surname, birthyear, city, email, phone)


name = "Алекс"
surname = "Иванов"
birthday = 1985
city = "Воронеж"
email = "Электропочта"
phone = "Телефон"

user_info(name, surname, birthday, city, email, phone)
