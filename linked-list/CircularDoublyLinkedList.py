class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node1.prev = node5

node2.next = node3
node2.prev = node1

node3.next = node4
node3.prev = node2

node4.next = node5
node4.prev = node3

node5.next = node1
node5.prev = node4
print("nTraversing forward!")
currentNode = node1
startNode = node1
print(currentNode.data, end=" -> ")
currentNode = currentNode.next
while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")
print("\nTraversing forward!")
currentNode = node5
startNode = node5
print(currentNode.data, end=" -> ")
currentNode = currentNode.prev
while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.prev
print("null")