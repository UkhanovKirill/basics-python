class Car:

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f"{self.name} едет"

    def stop(self):
        return f"{self.name} стоит"

    def turn(self, direction):
        return f"осуществляет поворот на {'лево' if direction == 0 else 'право'}"

    def show_speed(self):
        return f"{self.speed} км в час"

class TownCar(Car):

    def show_speed(self):
        return f"{self.speed} км в час (cкорость превышена)" if self.speed > 60 else f"{self.speed} км в час"


class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        return f"{self.speed} км в час (cкорость превышена)" if self.speed > 40 else f"{self.speed} км в час"

class PoliceCar(Car):

    def __init__(self, name, speed, color, is_police = True):
        super().__init__(name, speed, color, is_police)

sport = SportCar(input("Введите название спортивной машины "), int(input("Ее скорость ")), input("Ее цвет "))
town = TownCar(input("Введите название городской машины "), int(input("Ее скорость ")), input("Ее цвет "))
work = WorkCar(input("Введите название рабочей машины "), int(input("Ее скорость ")), input("Ее цвет "))
police = PoliceCar(input("Введите название полицейской машины "), int(input("Ее скорость ")), input("Ее цвет "))

print(f"Гоночная машина марки {sport.name} {sport.color} цвета {sport.turn(1)} со скоростью {sport.show_speed()}. За ней едет полицейская машина марки {police.name} {police.color} цвета со скоростью {police.show_speed()}.")
print(f"Авария. Предположительно {town.name} {town.color} цвета {town.turn(0)} со скоростью {town.show_speed()}, не замечая {work.name} {work.color} цвета двигавшегося со скоростью {work.show_speed()}")