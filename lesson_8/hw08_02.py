# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.
class ZeroDivError(Exception):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"Делитель = {self.num}, а на ноль делить нельзя!"


def division():
    try:
        dividend = int(input('Введите делимое >>> '))
        divider = int(input('Введите делитель >>> '))
        if 0 != divider:
            return dividend / divider
        else:
            raise ZeroDivError(divider)
    except ValueError:
        return "Нужно ввести целое число"
    except ZeroDivError as error:
        return error


print(division())
