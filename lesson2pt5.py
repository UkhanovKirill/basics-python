my_list = [1, 3, 5, 6, 8]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (000 - выход) "))
while digit != 000:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] > digit:
            my_list.insert(0, digit)
        elif my_list[-1] < digit:
            my_list.append(digit)
        elif my_list[el] < digit and my_list[el + 1] > digit:
            my_list.insert(el + 1, digit)
            break
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число (000 - выход) "))