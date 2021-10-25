# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class MyData:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_name(cls, day, month, year):
        cls.day = int(day)
        cls.month = int(month)
        cls.year = int(year)
        return

    @staticmethod
    def validator(day):
        try:
            if day < 1 or day > 31:
                return day
        except ValueError:
            print('Введите число от 1 до 31')

    @staticmethod
    def validator1(month):
        try:
            if month >= 1 or month <= 12:
                return month
        except ValueError:
            print('Введите число от 1 до 12')

    def __str__(self):
        return f'My data: {self.day}.{self.month}.{self.year}'


md = MyData(day=input('Input day:'), month=input('Input month:'), year=input('Input year:'))
print(md)

# с отработкой ошибок что-то упускаю.