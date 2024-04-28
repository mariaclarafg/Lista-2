import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

circle1 = Circle(5)

circle_area = circle1.area()
print("Circle area :", circle_area)
