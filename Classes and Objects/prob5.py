#Define a class Team with instance object variable a list of team emeber names.
# Provide methods to imput member names and display member names

class Team:
    def __init__(self):
        self.members = []

    def addMembers(self, names):
        self.members.append(names)

    def showMembers(self):
        print("Team Members :-")
        for i in self.members:
            print(i)

t1 = Team()
t1.addMembers("Rahul")
t1.addMembers("Rohan")
t1.addMembers("Sachin")
t1.showMembers()