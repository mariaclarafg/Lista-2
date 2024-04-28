import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def volume(self):
        return self.area() * self.height

cylinder = Cylinder(5, 10)
area = cylinder.area()
print(f"Area of the cylinder's base: {area:.2f}")
volume = cylinder.volume()
print(f"Cylinder's volume: {volume:.2f}")
