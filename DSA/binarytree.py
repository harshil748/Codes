class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_left(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            new_node = Node(key)
            new_node.left = self.root.left
            self.root.left = new_node

    def delete_right(self):
        if self.root and self.root.right:
            self.root.right = None

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=" ")

    def level_order(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.val, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert_left(1)
    tree.insert_left(2)
    tree.insert_left(3)
    tree.delete_right()

    print("Inorder Traversal:")
    tree.inorder(tree.root)
    print("\nPreorder Traversal:")
    tree.preorder(tree.root)
    print("\nPostorder Traversal:")
    tree.postorder(tree.root)
    print("\nLevel Order Traversal:")
    tree.level_order()
