class Stack:
    def __init__(stck):
        stck.items = []

    def push(stck, item):
        stck.items.append(item)

    def pop(stck):
        if not stck.is_empty():
            return stck.items.pop()
        return None

    def is_empty(stck):
        return len(stck.items) == 0

    def size(stck):
        return len(stck.items)


stack = Stack()
stack.push(2)
stack.push(3)
print(stack.pop())
stack.push(4)
print(stack.pop())
