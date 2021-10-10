# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное
# значение. При вызове функции должен создаваться объект-генератор. Функция должна вызываться
# следующим образом: for el in fact(n). Функция отвечает за получение факториала числа, а в
# цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
def generator(n):
    f_num = 1
    for i in range (2, n + 1):
        f_num *= i
        yield f_num


n = int(input('Введите число факториала: '))
for el in generator(n):
    print(el)