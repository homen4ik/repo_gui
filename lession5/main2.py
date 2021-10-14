# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке
with open('text_2.txt', 'r', encoding='utf-8') as f:
    my_line = f.readlines()
    for index, value in enumerate(my_line):
        number_word = len(value.split())
        print(f'Строка {index} содержит {number_word} слов')
