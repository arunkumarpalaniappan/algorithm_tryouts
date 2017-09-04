class BST:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.data = val

def insertToBst(root,value):
    if root is None:
        root = value
    else:
        if value.data < root.data:
            if root.left is None:
                root.left = value
            else:
                insertToBst(root.left, value)
        else:
            if root.right is None:
                root.right = value
            else:
                insertToBst(root.right, value)

def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)
 
def printGivenLevel(root , level):
    if root is None:
        return
    if level == 1:
        print "%d" %(root.data),
    elif level > 1 :
        if level%2 == 0 :
            printGivenLevel(root.right , level-1)
            printGivenLevel(root.left , level-1)
        else:
            printGivenLevel(root.left , level-1)
            printGivenLevel(root.right , level-1)

def height(node):
    if node is None:
        return 0
    else :
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1

tree = BST(5)
insertToBst(tree, BST(4))
insertToBst(tree, BST(6))
insertToBst(tree, BST(2))
insertToBst(tree, BST(1))
insertToBst(tree, BST(7))
insertToBst(tree, BST(8))
insertToBst(tree, BST(9))
insertToBst(tree, BST(10))

printLevelOrder(tree)