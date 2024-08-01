def selection_sort(array):                  # 
    n = len(array)                          # calculate the length of the array
    for i in range(n):                      # iterate through the array
        min_idx = i                         # set the minimum index to the current index
        for j in range(i+1, n):             # iterate through the array starting from the next index
            if array[j] < array[min_idx]:   # if the current element is less than the minimum element
                min_idx = j                 # set the minimum index to the current index
        temp = array[min_idx]               # swap the minimum element with the current element
        array[min_idx] = array[i]           # swap the minimum element with the current element
        array[i] = temp                     # swap the minimum element with the current element
    return array                            # return the sorted array

array = [64, 25, 12, 22, 11]
selection_sort(array)
print(array)