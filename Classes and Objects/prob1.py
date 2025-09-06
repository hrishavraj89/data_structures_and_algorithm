#Create a class Emplyee with attributes empid, name, salary and also define methods to access properties of Employee.

class Employee:
    def __init__(self, empid = None, name = None, salary = None):
        self.empid = empid
        self.name = name
        self.salary = salary

    def setEmpid(self, empid):
        self.empid = empid

    def setName(self, name):
        self.name = name

    def setSalary(self, salary):
        self.salary = salary

    def getEmpid(self):
        return empid
    
    def getName(self):
        return name
    
    def getSalary(self):
        return salary
    
e1 = Employee()
e2 = Employee(44, "Rahul", 40000)

e1.setEmpid(22)
e1.setSalary(50000)
e1.setName("Harsh")
print(e1.empid, e1.name, e1.salary)
print(e2.empid, e2.name, e2.salary)