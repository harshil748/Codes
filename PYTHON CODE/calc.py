def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    if n2!=0:
        return n1/n2
    else:
        return "Division by zero is not possible."
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
print("addition of numbers is: ",add(n1,n2))
print("substraction of numbers is: ",subtract(n1,n2))
print("multipliction of numbers is: ",multiply(n1,n2))
print("division of numbers is: ",divide(n1,n2))