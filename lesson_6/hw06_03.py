# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name: str
    surname: str
    position: str
    _income: {}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


john_smith = Position('John', 'Smith', 'driver', 70000, 36000)
artur_doe = Position('Artur', 'Doe', 'teacher', 80000, 15000)

print(f'{john_smith.get_full_name()}, {john_smith.position} - {john_smith.get_total_income()}')
print(f'{artur_doe.get_full_name()}, {artur_doe.position} - {artur_doe.get_total_income()}')
