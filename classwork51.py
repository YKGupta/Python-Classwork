# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
import math
class Circle:
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

ob = Circle(float(input("Enter radius of circle: ")))
print("Area:", ob.area())
print("Perimeter:", ob.perimeter())