def division(arg1, arg2):
    if arg2 != 0:
        return arg1 // arg2
    else:
        print("Второе число не может быть 0")
arg1 = int(input("Введите первое число: "))
arg2 = int(input("Введите второе число: "))
print(f'Результат:  {division(arg1, arg2)}')

