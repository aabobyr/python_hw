# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее
# 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить
# подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
count = 0
summ_salary: float = 0
data = []
with open('hw05_03_data.txt', encoding='utf-8') as my_file:
    for line in my_file:
        # print(line, end="") # построчно выводит сотрудника и оклад из файла
        salary = line.split(' ')
        if float(salary[1]) < 20000:
            data.append(salary[0])
        summ_salary += float(salary[1])
        count += 1

average = round(summ_salary / count, 2)
print('')
print(f'Сотрудники с окладом меньше 20000 - {data}')
print(f'Cредний доход всех {count} сотрудников - {average}')
