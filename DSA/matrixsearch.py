def search_in_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return -1

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = (left + right) // 2
        mid_element = matrix[mid // cols][mid % cols]

        if mid_element == target:
            return (mid // cols, mid % cols)
        elif mid_element < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


matrix = []
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print("Enter the matrix elements row-wise:")
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

target = int(input("Enter the target integer: "))
result = search_in_matrix(matrix, target)
if result != -1:
    print(f"Target found at index: {result}")
else:
    print("Target not found in the matrix.")
