def zero(arr):
    # Sort the array (bubble sort)
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # Reorder elements
    for i in range(1, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    # Print the result
    print(' '.join(str(num) for num in arr))

# Test the function
arr = [1, 5, 3, 7, 8, 2, 4, 6]
zero(arr)