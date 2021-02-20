class Road:
    def __init__(self, _length, _width, _thickness, _mass_1cm = 25):
        self._length = _length
        self._width = _width
        self._thickness = _thickness
        self._mass_1cm = _mass_1cm

    def mass(self):
        return self._length * self._width * self._thickness * self._mass_1cm

length = int(input("Введите длину дороги: "))
width = int(input("Введите ширину дороги: "))
thickness = int(input("Толщина полотна: "))
r = Road(length, width, thickness)
print(r.mass())