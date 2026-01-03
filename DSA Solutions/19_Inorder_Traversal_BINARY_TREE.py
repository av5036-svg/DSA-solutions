class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

inorder(root)
