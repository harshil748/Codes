def factorial(n):
    if n == 0 or n == 1:  # 2 comparison operation
        return 1  # 1 return operation

    result = 1  # 1 assignment operation
    for i in range(2, n + 1):  # Iterations: (n-1) times
        result *= i  # 2 operations per iteration

    return result


n = int(input())
print(factorial(n))
