def power(num, power):
    result = 1
    for i in range(power):
        result *= num
    return result

n = int(input("Enter a number: "))
p = int(input("Enter the power: "))
print(f"The result is {power(n, p)}")