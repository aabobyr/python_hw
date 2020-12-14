# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.
import datetime


class Date:
    def __init__(self, day):
        self.day = str(day)

    @classmethod
    def to_int(cls, day):
        try:
            day, month, year = [int(i) for i in day.split('-')]
            return day, month, year
        except ValueError:
            print(f'Дата {day} в некорректном формате, необходимо указать - dd-mm-yyyy!')
            exit(2)

    @staticmethod
    def valid(check_date):
        try:
            day, month, year = Date.to_int(check_date)
            datetime.date(year, month, day)
            return f'Дата введена корректно.'
        except ValueError:
            print(f'Введена некорректная дата - {day} - {month}, {year}!')
            exit(1)


print(Date.to_int('12-12-2020'))
# print(Date.to_int('13-13-2020'))
# print(Date.to_int('13-132020'))
# print(Date.valid('12-12-2020'))
# print(Date.valid('01-1980'))
print(Date.valid('15-132020'))
print(Date.valid('56-12-2008'))
