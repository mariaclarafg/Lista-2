class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
rectangle1 = Rectangle(5, 10)

rectangle_area = rectangle1.area()
print(f"Rectangle: {rectangle_area}")
