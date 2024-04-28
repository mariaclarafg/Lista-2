class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_data(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Maria", 19)
person2 = Person("Clara", 10)


person1.show_data()
person2.show_data()
