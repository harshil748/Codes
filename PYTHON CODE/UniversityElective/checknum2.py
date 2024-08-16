def classify_number(n):
    if n == 0:
        return "Zero"
    elif n > 0:
        return "Positive"
    else:
        return "Negative"

n = int(input("Enter a number: "))
print(f"The number {n} is classified as {classify_number(n)}.")