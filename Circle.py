import math 

class Circle: 
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return math.pi * self.radius ** 2



circle1 = Circle(42)

print(circle1.calculateArea())
