def insertion_sort_comparisons(array):
    n = len(array)
    comp = 0
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0:
            comp += 1
            if array[j] > key:
                array[j + 1] = array[j]
                j -= 1
            else:
                break
        array[j + 1] = key
    return comp


n = int(input())
arr = list(map(int, input().split()))
comparisons = insertion_sort_comparisons(arr)
print(comparisons)
