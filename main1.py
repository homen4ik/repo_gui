# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую
# их деление. Числа запрашивать у пользователя,предусмотреть обработку ситуации деления на ноль

x = int(input('Enter number: '))
y = int(input('Enter number: '))


def my_div(x, y):
    return x / y


if y !=0:
    print(my_div(x, y))
else:
    print("You can't divide by zero")
