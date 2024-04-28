class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_data(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, registration):
        super().__init__(name, age)
        self.registration = registration

    def show_data(self):
        print(f"Name: {self.name}, Age: {self.age}, Registration Number: {self.registration}")


student1 = Student("Maria Clara", 19, "20211IMI023")
student1.show_data()
