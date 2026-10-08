# Shape base class with an area() method
# Subclasses such as square, circle, triangle, etc ...
import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Main
c1 = Circle(7)
# c1 = Shape() #None
print(c1.area())
