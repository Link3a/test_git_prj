class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b
    def get_height(self):
        return self.a
    def get_widht(self):
        return self.b

from math import pi
class Circle:
    def _init_ (self, r):
        self.r = r
    def area(self):
        return pi * (self.r) ** 2

main_rect = Rectangle(5, 4)
print(main_rect.area())
main_Circle = Circle(2)
print(main_Circle.area())
