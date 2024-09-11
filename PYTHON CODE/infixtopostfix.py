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

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count


    def infix_to_postfix(expression):
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
        stack = []
        postfix = ""

    for ch in expression:
        if ch.isalpha():
            postfix += ch
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()
        else:
            while (
                stack
                and stack[-1] != "("
                and precedence[ch] <= precedence.get(stack[-1], 0)
            ):
                postfix += stack.pop()
            stack.append(ch)

    while stack:
        postfix += stack.pop()

    return postfix

expression = input("Enter the infix expression: ")
postfix_expression = infix_to_postfix(expression)
print("Postfix Expression:", postfix_expression)