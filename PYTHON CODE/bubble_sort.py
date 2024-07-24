array = [98, 56, 47 , 45, 78, 45, 6, 2, 12, 3]
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array
bubble_sort(array)
print(array)