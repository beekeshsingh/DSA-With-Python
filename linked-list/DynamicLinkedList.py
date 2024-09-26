class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Create a linked list
linklist = []
for i in range(1, 10):
    node = Node(i)
    linklist.append(node)
    if i > 1:
        linklist[i-2].next = node  # Correctly link the previous node's `next` to the current node

# Traverse and print the linked list
currentNode = linklist[0]
while currentNode:
    print(currentNode.data, end=" --> " if currentNode.next else "\n")
    currentNode = currentNode.next
