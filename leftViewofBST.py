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

def leftView(root,level,currentLevel):
    if not root:
        return
    else:
        if (currentLevel[0] < level):
            print root.data
            currentLevel[0] = level
    leftView(root.left, level+1, currentLevel)
    leftView(root.right, level+1, currentLevel)  
        
tree = BST(5)
insertToBst(tree, BST(4))
insertToBst(tree, BST(6))
insertToBst(tree, BST(2))
insertToBst(tree, BST(1))
insertToBst(tree, BST(7))
insertToBst(tree, BST(8))
insertToBst(tree, BST(9))
insertToBst(tree, BST(10))

leftView(tree, 1, [0])  # => 5,4,2,1,9,10 ,O(n)

