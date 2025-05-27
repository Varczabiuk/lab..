from abc import ABC, abstractmethod
import math

# Принцип відкритості/закритості (O): клас можна розширювати, але не змінювати
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Принцип єдиної відповідальності (S): кожен клас відповідає лише за свою фігуру
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Клас для обчислення площ усіх фігур
class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        return sum(shape.area() for shape in self.shapes)

# Точка входу
if __name__ == "__main__":
    shapes = [Circle(5), Rectangle(4, 6)]
    calculator = AreaCalculator(shapes)
    print("Загальна площа фігур:", calculator.total_area())