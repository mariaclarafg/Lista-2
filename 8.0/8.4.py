class Car:
    def __init__(self):
        self.speed = 0 

    def accelerate(self, my_list_time):
        acceleration = 10
        self.speed += acceleration * my_list_time
        print(f"Accelerating for {my_list_time} seconds. Current speed: {self.speed} m/s")

    def brake(self, my_list_time):
        deceleration = 5
        self.speed -= deceleration * my_list_time
        if self.speed < 0:
            self.speed = 0
        print(f"Braking for {my_list_time} seconds. Current speed: {self.speed} m/s")

car1 = Car()

car1.accelerate(5)
car1.brake(2)
car1.accelerate(3)