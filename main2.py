# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой

def people(*args):
    name = input('your name: ')
    last_name = input('your last name: ')
    year = input('your year of birth: ')
    city = input('your city: ')
    email = input('your email: ')
    phone = input('your phone: ')
    return name, last_name, year, city, email, phone


print(people())