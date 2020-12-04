# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    speed: str
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn_right(self):
        print(f'{self.name} повернула направо')

    def turn_left(self):
        print(f'{self.name} повернула налево')

    def show_speed(self):
        print(f'Текущая скорость {self.name} -- {self.speed}км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость town car {self.name} - {self.speed}км/ч')

        if self.speed > 60:
            print(f'town car {self.name} превышает разрешенную скорость')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость work car {self.name} -  {self.speed}км/ч')

        if self.speed > 40:
            print(f'Work car {self.name} превышает разрешенную скорость')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            print(f'{self.name} - полицейская машина')
        else:
            print(f'{self.name} - обычная машина')


bmw_m5 = SportCar(109, 'черный', 'bmw', False)
kia_rio = TownCar(68, 'черный', 'Киа рио', False)
truck = WorkCar(55, '', 'Поливалка', False)
traffic_police = PoliceCar(122, 'белая с синей полосой', 'Шкода', True)
print(f'Цвет {kia_rio.name} - {kia_rio.color}')
print(f'{bmw_m5.name} - полицейская машина? {bmw_m5.is_police}')
print(f'{traffic_police.name} - полицейская машины? {traffic_police.is_police}')
print(f'Цвет полицейской машины - {traffic_police.color}')

kia_rio.go()
kia_rio.turn_left()
bmw_m5.show_speed()
kia_rio.show_speed()
traffic_police.police()
traffic_police.show_speed()
truck.go()
truck.show_speed()
