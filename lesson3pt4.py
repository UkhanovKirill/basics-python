def my_func(x, y):
    if x > 0 and y < 0:
#        res = x ** y
        i = 1
        y = abs(y)
        res = x
        while i < y:
            res = res * x
            i = i + 1
            result = 1 / res
        return result
    elif x > 0 and y > 0:
        print("Вы ввели 2 положительных числа")
    elif x < 0 and y < 0:
        print("Вы ввели 2 отрицательных числа")
    elif x == 0 or y == 0:
        print("Одно из чисел равно 0")
    else: print("Нарушен порядок ввода")
number1 = int(input("Введите положительное число - "))
number2 = int(input("Введите отрицательное число - "))
print(my_func(number1, number2))