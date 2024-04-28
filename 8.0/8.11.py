class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_data(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def increase_salary(self, increase_percentage):
        self.salary *= (1 + increase_percentage / 100)

employee = Employee("Luiza", 40, 30000)
employee.increase_salary(10)
employee.show_data()
