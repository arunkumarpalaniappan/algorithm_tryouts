from singlyLinkedList import Node

def removeDulpicates(node):
    current = second = node
    while current != None:
        while second.next != None:
            if current.value == second.next.value:
                second.next = second.next.next
            else:
                second = second.next
        current = second = current.next
    return node

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(3)
    node4 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    node_r = removeDulpicates(node1)
    Node.traverse(node_r)