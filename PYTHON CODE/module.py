import basicopsmod

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")
print("Result:", basicopsmod.basic_op(a, b, op))
num = int(input("Enter a number to check even/odd: "))
print("Even or Odd:", basicopsmod.is_evenorodd(num))