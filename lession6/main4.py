#  Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
#  color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
#  что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar,
#  текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При
#  значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите
# результат.
class Car:

    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'Машина {self.name} поехала со скоростью {self.speed} км/ч')

    def stop(self, speed=0):
        self.speed = speed
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {"налево" if direction == 0 else "направл"}')

    def show_speed(self):
        return f'Скорость автомобился {self.name} {self.speed} км/ч'

class TownCar(Car):

    def show_speed(self):
        return f' Скорость {self.name} {self.speed} км/ч. Превышение скорости' \
            if self.speed > 60 else f'Скорость автомобиля {self.name} {self.speed} км/ч'

class WorkCar(Car):

    def show_speed(self):
        return f' Скорость {self.name} {self.speed} км/ч. Превышение скорости' \
            if self.speed > 40 else f'Скорость автомобиля {self.name} {self.speed} км/ч'

class PoliceCar(Car):

    is_police = True


town = TownCar(70, 'синий', 'BMW')
town.go()
town.show_speed()
town.turn(0)
town.stop()

work = WorkCar(40, 'оранжевый', 'Камаз')
work.go()
work.show_speed()
work.turn(20)
work.stop()

police = PoliceCar(90, 'белый', 'Ford')
police.go()
police.show_speed()
police.turn(90)
police.stop()

print(f'{town.name} - {town.color}, {work.name} - {work.color},{police.name} - {police.color}')
      