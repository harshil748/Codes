num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
addition = num1 + num2
subtraction = num1 - num2
division = num1 / num2
multiplication = num1 * num2
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Division:", division)
print("Multiplication:", multiplication)

if addition == int(addition):
    addition = int(addition)
if subtraction == int(subtraction):
    subtraction = int(subtraction)
if division == int(division):
    division = int(division)
if multiplication == int(multiplication):
    multiplication = int(multiplication)
    
print("Data type of addition:", type(addition))
print("Data type of subtraction:", type(subtraction))
print("Data type of division:", type(division))
print("Data type of multiplication:", type(multiplication))
# Practical 1.7