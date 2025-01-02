def fibonacci_sequence(n):
    def generate_fibonacci(limit, a=0, b=1, sequence=None):
        if sequence is None:  # Input valid 1-2 comparison operation
            sequence = []
        if a > limit:  # Termination condition 1 comparison
            return sequence  # 1 return operation
        sequence.append(a)  # append 1 operation
        return generate_fibonacci(limit, b, a + b, sequence)
        # Recursive call 3 operations
        # 1. parameter passing
        # 2. recursive function call
        # 3. return result
    if n < 0 or n >= 100:  # Input valid 2 comparisons
        raise ValueError("Input must be between 0 and 99")
    return generate_fibonacci(n)

n = int(input())
print(*fibonacci_sequence(n))