def fibonacci_sequence(n):
    def generate_fibonacci(limit, a=0, b=1, sequence=None):
        if sequence is None:
            sequence = []

        if a > limit:
            return sequence

        sequence.append(a)

        return generate_fibonacci(limit, b, a + b, sequence)

    if n < 0 or n >= 100:
        raise ValueError("Input must be between 0 and 99")

    return generate_fibonacci(n)


n = int(input())

print(*fibonacci_sequence(n))
