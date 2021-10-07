# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    return sum((arg1, arg2, arg3)) - min(arg1, arg2, arg3)


print(my_func(4, 9, 7))