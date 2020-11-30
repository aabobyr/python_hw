# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
# о фирме: название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с
# фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков). Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

result_list = []
firm_profit = {}
profit = 0
prof_average_int = 0
count = 0
with open('hw05_07_data.txt', encoding='utf-8') as data_file:
    for line in data_file:
        name, form_property, income, costs = line.split()
        firm_profit[name] = round(float(income) - float(costs), 2)
        if firm_profit.get(name) > 0:
            profit += firm_profit.get(name)
            count += 1

    result_list.append(firm_profit)

    if count != 0:
        result_list.append({'Cредняя прибыль': (round(profit / count, 2))})
    else:
        print(f'Все компании не прибыльны')
    print(f'{result_list}')

with open('hw05_07.json', 'w', encoding="utf-8") as json_file:  # создаем json
    json.dump(result_list, json_file, ensure_ascii=False)

print(f'\n Итоговый список сохранен в файл - {json_file.name}\n')

with open('hw05_07.json', encoding="utf-8") as json_file:  # открываем json, чтобы распечатать
    result = json.load(json_file)

print(result)
