def generate_binary_numbers(n):
    queue = []
    queue.append("1")

    for _ in range(n):
        binary_number = queue.pop(0)
        print(binary_number)
        queue.append(binary_number + "0")
        queue.append(binary_number + "1")


n = int(input("Enter a positive integer: "))
generate_binary_numbers(n)