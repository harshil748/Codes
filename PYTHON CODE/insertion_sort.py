array = [5, 2, 4, 6, 1, 3]
def insertion_sort(array):
    n = len(array)                          # calculate the length of the array
    first = 0                               # set the first index to 0
    second = 0                              # set the second index to 0
    for i in range(1, n):                   # iterate through the array starting from the second index
        key = array[i]                      # set the key to the current element       
        j = i - 1                           # set the index to the previous index
        while j >= 0 and array[j] > key:    # while the index is greater than or equal to 0 and the current element is greater than the key
            array[j + 1] = array[j]         # set the next element to the current element
            j -= 1                          # decrement the index
        array[j + 1] = key                  # set the next element to the key
    return array
insertion_sort(array)
print(array)