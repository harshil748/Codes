class Stack:
    def __init__(self):
        self.stack = [] 
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def isvalid(string : str) -> bool:
        stack = []
        for char in string:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                if not stack:
                    return False
                current_char = stack.pop()
                if current_char == '(':
                    if char != ')':
                        return False
                if current_char == '[':
                    if char != ']':
                        return False
                if current_char == '{':
                    if char != '}':
                        return False
        return len(stack) == 0
    
stack = Stack()
print(isvalid("([)])))"))