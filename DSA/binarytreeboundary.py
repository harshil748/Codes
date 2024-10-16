class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printBoundary(root):
    if not root:
        return []

    boundary = [root.val]

    def leftBoundary(node):
        if node:
            if node.left:
                boundary.append(node.val)
                leftBoundary(node.left)
            elif node.right:
                boundary.append(node.val)
                leftBoundary(node.right)

    def leaves(node):
        if node:
            leaves(node.left)
            if not node.left and not node.right:
                boundary.append(node.val)
            leaves(node.right)

    def rightBoundary(node):
        if node:
            if node.right:
                rightBoundary(node.right)
                boundary.append(node.val)
            elif node.left:
                rightBoundary(node.left)
                boundary.append(node.val)

    leftBoundary(root.left)
    leaves(root.left)
    leaves(root.right)
    rightBoundary(root.right)

    return boundary


root = TreeNode(20)
root.left = TreeNode(8)
root.left.left = TreeNode(4)
root.left.right = TreeNode(12)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)
root.right = TreeNode(22)
root.right.right = TreeNode(25)

print(printBoundary(root))  
