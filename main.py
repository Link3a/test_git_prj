from math import pi

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

    def set_height(self, a):
        self.a = a
    def set_weight(self, b):
        self.b = b

    def perimeter(self):
        return self.a * 2 + self.b * 2


class Circle:
    def __init__ (self, r):
        self.r = r
    def area(self):
        return pi * (self.r) ** 2

main_rect = Rectangle(5, 4)
print(main_rect.area())
print(main_rect.perimeter())
main_Circle = Circle(2)
print(main_Circle.area())
