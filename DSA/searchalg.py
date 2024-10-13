def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr1 = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", arr1)
bubble_sort(arr1)
print("Sorted array using Bubble Sort:", arr1)

arr2 = [5, 2, 8, 1, 9, 4, 3, 7, 6]
print("Unsorted array:", arr2)
selection_sort(arr2)
print("Sorted array using Selection Sort:", arr2)

arr3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Unsorted array:", arr3)
insertion_sort(arr3)
print("Sorted array using Insertion Sort:", arr3)
