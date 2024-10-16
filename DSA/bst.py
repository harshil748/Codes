class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertNode(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insertNode(root.left, val)
    else:
        root.right = insertNode(root.right, val)
    return root


def searchBST(root, val):
    if not root or root.val == val:
        return root
    if val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)


def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val, end=" ")
        inorderTraversal(root.right)


root = TreeNode(10)
insertNode(root, 5)
insertNode(root, 15)
insertNode(root, 3)
insertNode(root, 7)
insertNode(root, 12)
insertNode(root, 18)

print("In-order traversal of the BST:")
inorderTraversal(root)
print()

result = searchBST(root, 7)
if result:
    print(f"Subtree rooted at node with value {result.val}:")
    inorderTraversal(result)
else:
    print("Value not found in the BST.")
