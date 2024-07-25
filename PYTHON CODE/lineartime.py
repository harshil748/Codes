array = [3, 8, 6, 7, 5, 9]
'''
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
'''
def linear_time(array):
    n = len(array)
    first = 0 
    second = 0
    for i in range(n-1):
     if array[i] > array[i+1]:
        first = i
        break
    for i in range(n-1, first, -1):
        if array[i] < array[i-1]:
            second = i
            break
    for i in range(n-1):
        temp = array[first]
        array[first] = array[second]
        array[second] = temp
    return array
        
linear_time(array)
print(array)