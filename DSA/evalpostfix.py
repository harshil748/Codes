def evaluate_postfix(expression):
    stack = []
    for char in expression.split():
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == "+":
                stack.append(operand1 + operand2)
            elif char == "-":
                stack.append(operand1 - operand2)
            elif char == "*":
                stack.append(operand1 * operand2)
            elif char == "/":
                stack.append(operand1 / operand2)
    return stack[0]

expression = input("Enter the postfix expression: ")
print("The entered post expression is: "+expression)
result = evaluate_postfix(expression)
print("The ans is : ",result)