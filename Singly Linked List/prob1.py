#Define a class Node to describe a node of singly linked list.

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)

node1.next = node2

print(node1.data)
print(node1.next.data)