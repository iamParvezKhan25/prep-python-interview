from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area():
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


sq_obj = Square(5)
cir_obj = Circle(10)

print(sq_obj.area())
print(cir_obj.area())