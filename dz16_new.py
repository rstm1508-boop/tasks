class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age
    
class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self._position = position

    @property
    def position(self):
        return self._position
    
    def display_into(self):
        print(f"{self.name}, Возраст: {self.age}, Должность: {self.position}")

class Manager(Employee):
    def __init__(self, name, age, position):
        super().__init__(name, age, position)
        self._team = []

    @property
    def team(self):
        return self._team
    
    def add_employee_to_team(self, employee):
        if isinstance(employee, Employee):
            self._team.append(employee)
        else:
            raise ValueError("Только сотрудники могут быть добавлены в команду")
    
    def display_team_into(self):
        print(f"Команда менеджера {self.name}:")
        for emp in self.team:
            emp.display_info()

def main():
    employees = {}
    managers = {}

    while True:
        print("\nМенеджмент персонала:")
        print("1. Добавить нового сотрудника")
        print("2. Назначить сотрудника в команду менеджера")
        print("3. Показать всех сотрудников и менеджеров")
        print("4. Выход")
        
        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            name = input("Имя сотрудника: ")
            try:
                age = int(input("Возраст сотрудника: "))
                position = input("Должность сотрудника: ")
                
                # Создаем объект класса Employee или Manager
                if position.lower() == "менеджер":
                    new_employee = Manager(name, age, position)
                    managers[name] = new_employee
                else:
                    new_employee = Employee(name, age, position)
                    employees[name] = new_employee
                    
                print(f"Сотрудник {name} успешно добавлен.")
            
            except ValueError:
                print("Ошибка: неверный ввод возраста.")

        elif choice == '2':
            manager_name = input("Имя менеджера: ")
            employee_name = input("Имя сотрудника: ")

            if manager_name not in managers or employee_name not in employees:
                print("Ошибка: менеджер или сотрудник не найдены.")
            else:
                manager = managers[manager_name]
                employee = employees[employee_name]
                manager.add_employee_to_team(employee)
                print(f"Сотрудник {employee_name} назначен в команду менеджера {manager_name}.")

        elif choice == '3':
            print("\nСотрудники:")
            for emp in employees.values():
                emp.display_info()

            print("\nМенеджеры и их команды:")
            for man in managers.values():
                man.display_info()
                man.display_team_info()

        elif choice == '4':
            break

if __name__ == "__main__":
    main()