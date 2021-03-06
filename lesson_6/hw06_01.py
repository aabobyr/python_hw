# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.
from time import sleep


class TrafficLight:
    __color: str
    colors = ('красный', 'желтый', 'зеленый')

    def __init__(self, __color):
        self.__color = __color

    def switch(self):
        i = 0
        for x in self.colors:
            if x == self.__color.lower():
                i = self.colors.index(x)
            elif self.__color != "":
                print(f'Цвет {self.__color} не входит в список цветов светофора')
                exit('Передан неверный цвет')
        while i < 3:
            print(f'Светофор - {TrafficLight.colors[i]}')
            if i == 0:
                sleep(7)
                i += 1
            elif i == 1:
                sleep(2)
                i += 1
            elif i == 2:
                sleep(3)
                if input("Чтобы остановить работу светофора, нажмите 'n' >>>").lower() == 'n':
                    break
                else:
                    i = 0


# traffic_light = TrafficLight('зеленый')
#traffic_light = TrafficLight('Желтый')
traffic_light = TrafficLight('розовый')

traffic_light.switch()
