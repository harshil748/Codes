def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        temp = array[min_idx]
        array[min_idx] = array[i]
        array[i] = temp
    return array

array = [64, 25, 12, 22, 11]
selection_sort(array)
print(array)