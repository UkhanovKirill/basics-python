class MyZeroDivisionError(Exception):
    text = "Деление на ноль запрещено"

    def __str__(self):
        return self.text

class Number(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise MyZeroDivisionError

        return Number(float(self) / float(other))


while True:
    try:
        dividend, divider = map(Number, input("Введите делимое и делитель через пробел: ").split())
        print(dividend / divider)
    except MyZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
        break
