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

main_rect = Rectangle(5, 4)
print(main_rect.area())
