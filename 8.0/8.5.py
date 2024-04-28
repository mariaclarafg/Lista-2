class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} makes a generic animal sound.")

animal1 = Animal("Turtle", 12)

animal1.make_sound()
