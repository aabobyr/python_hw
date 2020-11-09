# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и
# секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

seconds = (input("Введите время в секундах >>>"))

if not seconds.isdigit():
    print("Неверный формат числа")
    exit()

minutes = seconds // 60
hours = minutes // 60

print(f'Время {hours:02d}:{minutes % 60:02d}:{seconds % 60:02d}')