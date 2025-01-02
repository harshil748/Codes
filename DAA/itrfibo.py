def fibonacci_sequence(n):
    if n <= 0:
        return []

    fib_seq = [0, 1]

    while True:
        next_num = fib_seq[-1] + fib_seq[-2]

        if next_num > n:
            break

        fib_seq.append(next_num)

    return fib_seq


n = int(input())

print(*fibonacci_sequence(n))
