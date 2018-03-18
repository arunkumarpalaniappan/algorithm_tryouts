from doublyLinkedList import Node

def traverse(node):
    while node != None:
        print node.value
        traverse(node.prev)
        traverse(node.next)

if __name__ == "main":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node3.next = node4
    node4.next = node5
    node5.next = None
    node5.prev = node4
    node4.prev = node3
    node3.prev = node2
    node2.prev = node1
    node1.prev = None
    node1.next = node2
    node2.next = node3

    traverse(node3)