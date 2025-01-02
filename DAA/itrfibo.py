def fibonacci_sequence(n):
    if n <= 0:  # input valid 1-2 comparison operations
        return []  # 1 return operation

    fib_seq = [0, 1]  # Initial 2 operations

    while True:
        next_num = fib_seq[-1] + fib_seq[-2]  
        # Last two element : 2 operations
        # Addition operation: 1

        if next_num > n:  # Comparison : 1 operation
            break

        fib_seq.append(next_num)  # Append operation: 1

    return fib_seq


n = int(input())

print(*fibonacci_sequence(n))