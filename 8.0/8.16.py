class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

class RightTriangle(Triangle):
    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)

    def area(self):
        s = self.perimeter() / 2
        area = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
        return area

right_triangle = RightTriangle(3, 4, 5)
perimeter = right_triangle.perimeter()
print(f"Perimeter of the right triangle: {perimeter}")
area = right_triangle.area()
print(f"Area of the right triangle: {area}")
