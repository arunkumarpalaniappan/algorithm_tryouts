class BST:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def insertIntoBST(root, value):
    if root is None:
        root = value
    else:
        if value.data < root.data:
            if root.left is None:
                root.left = value
            else:
                insertIntoBST(root.left, value)
        else:
            if root.right is None:
                root.right = value
            else:
                insertIntoBST(root.right, value)

tree = BST(7)
insertIntoBST(tree, BST(3))
insertIntoBST(tree, BST(8))

print tree
