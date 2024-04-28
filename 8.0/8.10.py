class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_data(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Client(Person):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

    def show_data(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

client = Client("Maria Clara", 19, "999 Ipanema")

client.show_data()
