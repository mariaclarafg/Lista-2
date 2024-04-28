class Vehicle:
    def __init__(self):
        self.speed = 0

    def accelerate(self, acceleration):
        self.speed += acceleration

    def brake(self, deceleration):
        self.speed -= deceleration
        if self.speed < 0:
            self.speed = 0

    def show_speed(self):
        print(f"Current speed: {self.speed} km/h")


class Car(Vehicle):
    def __init__(self, brand):
        super().__init__()
        self.brand = brand

car = Car("FIAT")
car.accelerate(90)
car.show_speed()

car.brake(20)
car.show_speed()
