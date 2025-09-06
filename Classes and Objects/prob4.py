# Define a class Rectangle with length and breadth as instance object variables.
# Provide setDimensions(), showDimensions(), and getArea() method in it.

class Rectangle:
    def __init__(self, length = None, breadth = None):
        self.length = length
        self.breadth = breadth

    def setDimensions(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def getDimensions(self):
        return (self.length, self.breadth)
    
    def showDimension(self):
        print(f"The length is {self.length}cm and breadth is {self.breadth}cm.")

    def getArea(self):
        print(f"The area is {self.length * self.breadth}cm.")

c1 = Rectangle(2, 3)
c1.setDimensions(20, 30)
c1.showDimension()
c1.getArea()