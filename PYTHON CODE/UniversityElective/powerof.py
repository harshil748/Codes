def power(base, exponent):
    result = 1
    while exponent > 0:
        result *= base
        exponent -= 1
    return result

num = int(input("Enter the number:"))
power_of = int(input("Enter the power:"))
print('Power is ', power(num, power_of))