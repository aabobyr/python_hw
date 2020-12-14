# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. Подсказка:
# постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по
# ООП.
class CapacityException(Exception):
    def __init__(self, capacity):
        self.capacity = capacity

    def __str__(self):
        return f'Достигнута максимальная емкость склада -  {self.capacity}!'


class Warehouse:
    capacity: int
    inventory: list
    __count: int

    def __init__(self, capacity=0):
        self.capacity = capacity
        self.inventory = []
        self.__count = 0

    def store_receipt(self, cls):
        if self.__count < self.capacity:
            self.inventory.append(cls)
            self.__count += 1
        else:
            raise CapacityException(self.capacity)

    def move_to_head_office(self, qty):
        if qty > 0:
            try:
                item = str(f'В головную организацию передан: \n {self.inventory[qty - 1]}')
                self.inventory.pop(qty - 1)
                print(item)
            except IndexError:
                print(f'На складе только {len(self.inventory)} шт. техники')
        else:
            print(f'Введено отрицательно число или ноль, перемещать нечего')

    def print_inventory(self):
        return "\n".join(
            str(item)
            for item in self.inventory
        )


class OfficeEquipment:
    name: str
    price: float

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Printer(OfficeEquipment):
    print_type: str
    print_quality: str

    def __init__(self, name, price, print_type, print_quality):
        super().__init__(name, price)
        self.print_type = print_type
        self.print_quality = print_quality

    def __str__(self):
        return f'{self.name}, цена - {self.price}, тип печати - {self.print_type}, качество печати - {self.print_quality} '


class Scanner(OfficeEquipment):
    scan_resolution: str

    def __init__(self, name, price, resolution):
        super().__init__(name, price)
        self.scan_resolution = resolution

    def __str__(self):
        return f'{self.name}, цена - {self.price}, разрешение сканирования - {self.scan_resolution}'


class Copier(OfficeEquipment):
    qty_of_lists: int
    resolutions: str

    def __init__(self, name, price, qty_of_lists, resolution):
        super().__init__(name, price)
        self.qty_of_lists = qty_of_lists
        self.resolution = resolution

    def __str__(self):
        return f'{self.name}, цена - {self.price}, количество листов - {self.qty_of_lists},разрешение сканирования -{self.resolution}'


epson = Printer('epson', 5499, 'струйный', 'фото')
hp = Copier('hp DeskJet f4283', 3899.99, 100, '600dpi')
canon = Scanner('Canon LiDE 300', 5490, '2400x2400dpi')

stock = Warehouse(2)

stock.store_receipt(epson)
stock.store_receipt(hp)
print(stock.print_inventory())
print()
try:
    stock.store_receipt(canon)
except CapacityException as exception:
    print('Достигнута максимальная емкость склада')
print()
print(f'На складе находятся \n {stock.print_inventory()}')
print()

try:
    move_qty = int(input(f'Введите сколько единиц оргтехники нужно переместить в головную компанию >>> '))
    stock.move_to_head_office(move_qty)
except ValueError:
    print(f'Нужно ввести целое число')
