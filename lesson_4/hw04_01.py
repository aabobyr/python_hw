# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

import sys

try:
    file, work_hours, rate_per_hour, reward = sys.argv
    salary = float(work_hours) * float(rate_per_hour) + float(reward)
    print(f'Salary = {round(salary, 2)} y.e.')
except ValueError:
    print("Invalid args. You have to specify three arguments")
    exit()
