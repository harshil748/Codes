def linear_search(arr, x):
    comp = 0
    for i in range(len(arr)):
        comp += 1
        if arr[i] == x:
            return i + 1, comp
    return -1, comp


def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    comp = 0
    result = -1
    while low <= high:
        comp += 1
        mid = (low + high) // 2
        if arr[mid] == x:
            result = mid + 1
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return result if result != -1 else -1, comp


n = int(input())
arr = list(map(int, input().split()))
x = int(input())
linear_result, linear_comparisons = linear_search(arr, x)
binary_result, binary_comparisons = binary_search(arr, x)
print(linear_result, linear_comparisons, binary_comparisons)