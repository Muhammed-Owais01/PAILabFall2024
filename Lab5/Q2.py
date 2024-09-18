from abc import ABC, abstractmethod

# Create abstract base class "shape" that has abstract method "area". Inherit rectangle, triangle
# and square class from shape class and provide implementation of "area" method for each
# derived class. Finally print area of rectangle, triangle and square.


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, height, length):
        self.height = height
        self.length = length

    def area(self):
        return 0.5* self.length* self.height

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

rect1 = Rectangle(2,3)
sq1 = Square(4)
tr1 = Triangle(5, 2)

print(f"Rectangle: {rect1.area()}\n"
      f"Triangle: {tr1.area()}\n"
      f"Square: {sq1.area()}")