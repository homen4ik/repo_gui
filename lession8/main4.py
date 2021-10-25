# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
# будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
# классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для
# каждого типа оргтехники.

class OfficeEquipment:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f'{self.brand} {self.model} - {self.price}$'


class Printers(OfficeEquipment):
    def to_print(self, types, speed, color):
        self.types = types  # струйный, лазерный
        self.speed = speed  # скорость печати лист/мин
        self.color = color # цветной, монохромный


class Scanners(OfficeEquipment):
    def to_scan(self, speed):
        self.speed = speed  #планшетный, проекционный


class Xerox(OfficeEquipment):
    def to_copy(self, form, color):
        self.form = form   # формат печати (А4, А3)
        self.color = color # цветной, монохромный

