class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def findLowestValue(head):
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue

node1 = Node(10)
node2 = Node(7)
node3 = Node(30)
node4 = Node(1)
node5 = Node(18)
node6 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print("The lowest value in the linked list is:", findLowestValue(node1))