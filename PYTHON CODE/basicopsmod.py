def basic_op(a,b,op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return None

def is_evenorodd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"