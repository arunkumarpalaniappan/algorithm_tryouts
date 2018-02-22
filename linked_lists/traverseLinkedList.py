class Node:
    def __init__(self,value):
            self.value = value
            self.next = None
            
def traverse(node):
    while node != None:
        print node.value
        node = node.next

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    traverse(node1)