name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
year = int(input('Введите ваш год рождения: '))
city = input('Введите город проживания: ')
email = input('Введите вашу почту: ')
telephone = input('Введите ваш телефон: ')
def my_func(**kwargs):
    return print(kwargs)
my_func(name = name, surname = surname, year = year, city = city, email = email, telephone = telephone)
