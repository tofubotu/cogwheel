class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return "Node:{} -> next ID:{}".format(self.data,id(self.next))

# Lingitud noded
node1 = Node("X")
node2 = Node(2)
node3 = Node("Unknown Node")

# Loome lingi
node1.next = node2
node2.next = node3

# m88da linke k2ima
current_node = node1
while current_node:
    print(current_node)
    current_node = current_node.next
