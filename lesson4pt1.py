def sal():
    time = int(input('Выработка в часах '))
    salary = int(input('Ставка '))
    bonus = int(input('Премия '))
    res = time * salary + bonus
    print(f'заработная плата сотрудника  {res}')
sal()