array = [5, 2, 4, 6, 1, 3]
def insertion_sort(array):
    n = len(array)
    first = 0
    second = 0
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
insertion_sort(array)
print(array)