#Define a class Circle with instance object variable radius. Provide ssetter and getter
#for radius. Also define getArea() and getCircumference() methods.

class Circle:
    def __init__(self, radius = None):
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius
    
    def getArea(self):
        print(f"The area is {2 * 3.14 * self.radius * self.radius}")

    def getCircumference(self):
        print(f"The circumference is {2 * 3.14 * self.radius}")

c1 = Circle(2)
c1.getArea()
c1.getCircumference()