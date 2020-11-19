# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В
# программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем
# регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func().

# легкий способ работает и с несколькими словами в строке
def int_func(text):
    return text.title()


# word = 'winter'
word = 'лето работа'
print(int_func(word))

list_word = 'лето работа стол'


# способ без функции title
def int_func_hard(text):
    words = text.split(' ')
    upper_words = []
    for i in words:
        element = str(i)
        first_letter = element[:1].upper()
        word = first_letter + element[1:]
        upper_words.append(word)
    return ' '.join(upper_words)


print(int_func_hard(list_word))
