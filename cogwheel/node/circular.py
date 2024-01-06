class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 9 node luua
nodes = [Node(i) for i in range(1, 10)]

# lingid
for i in range(9):
    link = (i + 1) % 9
    print("current index:{} -> next index -> {}".format(i,link))
    nodes[i].next = nodes[link]

# loeme ringliikumisi
def traverse_and_count_circles(start_node, max_circles):
    current_node = start_node
    count = 0
    circles = 0

    while circles < max_circles:
        count += 1
        current_node = current_node.next
        # kuvame ring massiivi id ja next id (peab olema l6p j2rgmise rea algus)
        print("current:{} next:{}".format(id(current_node), id(current_node.next)))
        # count algusest
        if current_node == start_node:
            circles += 1
            print(f"Completed {circles} circle(s)")

    return circles

max_circles = 5
traverse_and_count_circles(nodes[0], max_circles)
