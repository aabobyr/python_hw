first_distance = int(input("Введите результат за первый день >>>"))
target = int(input("Введите результат, которого должен достичь спортсмен >>>"))

qty_days = 1

while target > first_distance:
    qty_days += 1
    #first_distance = first_distance * 1.1
    first_distance += first_distance * .1

print(qty_days)
