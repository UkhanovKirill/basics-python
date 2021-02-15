MINIMAL_SALARY = 20000
print("Зарплата меньше 20000:")
with open('text_3.txt', 'r', encoding = "utf-8") as file:
    employees = file.readlines()
summ_salary = 0
for employee in employees:
    name, salary = employee.split()
    salary = float(salary)
    summ_salary += salary
    if salary < MINIMAL_SALARY:
        print(name)
print('Средняя зарплата: ', round(summ_salary / len(employees), 2))
