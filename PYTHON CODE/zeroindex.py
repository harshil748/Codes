array = [1, 2, 3, 4, 5, 6]
def zero(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                
        for j in range(1, len(array) - 1, 2):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
zero(array)
print(array)