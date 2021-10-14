# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('text_5.txt', 'w', encoding='utf-8') as f:
    f.write(f"{''.join([str(i) for i in range(1, 11)])}")

with open('text_5.txt', 'r', encoding='utf-8') as f:
    numbers = [int(i) for i in f.read().split()]
    print(sum(numbers))
    