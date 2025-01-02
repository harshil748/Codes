def factorial(n):
    if n == 0 or n == 1:  # 2 comparison operation
        return 1  # 1 return operation

    return n * factorial(n - 1)
    # 3 operations
    # 1. multiplication
    # 2. recursive function call
    # 3. return result

n = int(input())
print(factorial(n))
