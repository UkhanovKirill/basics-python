def my_sum ():
    sum_res = 0
    x = 0
    while x == 0:
        number = input('Введите числа через пробел, нажмите Q для выхода: ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                x = 1
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма чисел равна {sum_res}')
    return
my_sum()