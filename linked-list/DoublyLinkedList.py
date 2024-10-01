
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(12)
node2 = Node(2)
node3 = Node(5)
node4 = Node(21)
node5 = Node(1)

node1.next = node2

node2.next = node3
node2.prev = node1

node3.next = node4
node3.prev = node2

node4.next = node5
node4.prev = node3

node5.prev = node4

print("\nTraversing forward:")
currentNode = node1
while currentNode:
    print(currentNode.data, end=" --> ")
    currentNode = currentNode.next
print("null")

print("\nTraversing backward:")
currentNodeBack = node5
while currentNodeBack:
    print(currentNodeBack.data, end=" --> ")
    currentNodeBack = currentNodeBack.prev
print("null")