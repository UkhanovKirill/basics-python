class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

a = Position(input("Имя: "), input("Фамилия: "), input("Должность: "), int(input("Зарплата: ")), int(input("Премия: ")))
print(a.get_full_name())
print(a.position)
print(a.get_total_income())