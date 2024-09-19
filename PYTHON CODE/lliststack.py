class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count


stack = Stack()
stack.push(2)
stack.push(3)
print(stack.pop())
stack.push(4)
print(stack.pop())