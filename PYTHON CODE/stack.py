class Stack:
    def isValid(self, string: str) -> bool:
        stack = []
        for char in string:
            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                if not stack:
                    return False
                current_char = stack.pop()
                if current_char == "(":
                    if char != ")":
                        return False
                if current_char == "[":
                    if char != "]":
                        return False
                if current_char == "{":
                    if char != "}":
                        return False
        return len(stack) == 0

stack = Stack()
print("( Char is: "+ str(stack.isValid("(")))
print(") Char is: " + str(stack.isValid(")")))
print("[ Char is: " + str(stack.isValid("[")))
print("] Char is: " + str(stack.isValid("]")))
print("{ Char is: " + str(stack.isValid("{")))
print("} Char is: " + str(stack.isValid("}")))
print("() Char is: " + str(stack.isValid("()")))
print("[] Char is: " + str(stack.isValid("[]")))
print("{} Char is: " + str(stack.isValid("{}")))