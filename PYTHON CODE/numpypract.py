import numpy as np

# np.array(): Create a NumPy array from a list or tuple
print("\n=== np.array() ===")
list_array = np.array([1, 2, 3, 4, 5])
tuple_array = np.array((6, 7, 8, 9, 10))
print("From list:", list_array)
print("From tuple:", tuple_array)

# np.zeros(): Create an array filled with zeros
print("\n=== np.zeros() ===")
zeros_1d = np.zeros(5)  # 1D array of 5 zeros
zeros_2d = np.zeros((3, 4))  # 3x4 array of zeros
print("1D zeros:", zeros_1d)
print("2D zeros:\n", zeros_2d)

# np.ones(): Create an array filled with ones
print("\n=== np.ones() ===")
ones_1d = np.ones(5)  # 1D array of 5 ones
ones_2d = np.ones((2, 3))  # 2x3 array of ones
print("1D ones:", ones_1d)
print("2D ones:\n", ones_2d)

# np.arange(): Create an array with a range of values
print("\n=== np.arange() ===")
arange_ex1 = np.arange(10)  # 0 to 9
arange_ex2 = np.arange(2, 10)  # 2 to 9
arange_ex3 = np.arange(2, 20, 2)  # 2 to 18 with step 2
print("arange(10):", arange_ex1)
print("arange(2, 10):", arange_ex2)
print("arange(2, 20, 2):", arange_ex3)

# np.linspace(): Create an array with evenly spaced values over a specified interval
print("\n=== np.linspace() ===")
linspace_ex = np.linspace(0, 1, 5)  # 5 evenly spaced values from 0 to 1
print("linspace(0, 1, 5):", linspace_ex)

# np.reshape(): Change the shape of an array without changing its data
print("\n=== np.reshape() ===")
original = np.arange(12)
reshaped = original.reshape(3, 4)  # Reshape to 3x4
print("Original:", original)
print("Reshaped to 3x4:\n", reshaped)

# np.flatten(): Convert a multi-dimensional array into a 1D array
print("\n=== np.flatten() ===")
multi_dim = np.array([[1, 2, 3], [4, 5, 6]])
flattened = multi_dim.flatten()
print("Multi-dimensional array:\n", multi_dim)
print("Flattened array:", flattened)

# np.transpose(): Transpose an array (swap rows and columns)
print("\n=== np.transpose() ===")
matrix = np.array([[1, 2, 3], [4, 5, 6]])
transposed = np.transpose(matrix)  # or matrix.T
print("Original matrix:\n", matrix)
print("Transposed matrix:\n", transposed)

# np.concatenate(): Join two or more arrays along an axis
print("\n=== np.concatenate() ===")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concated = np.concatenate((arr1, arr2))
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Concatenated:", concated)

# np.split(): Split an array into multiple sub-arrays
print("\n=== np.split() ===")
array_to_split = np.array([1, 2, 3, 4, 5, 6])
splits = np.split(array_to_split, 3)
print("Original array:", array_to_split)
print("Split into 3:", [arr for arr in splits])

# np.vstack(): Stack arrays vertically (row-wise)
print("\n=== np.vstack() ===")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
vertical = np.vstack((a, b))
print("Array 1:", a)
print("Array 2:", b)
print("Vertical stack:\n", vertical)

# np.hstack(): Stack arrays horizontally (column-wise)
print("\n=== np.hstack() ===")
horizontal = np.hstack((a, b))
print("Array 1:", a)
print("Array 2:", b)
print("Horizontal stack:", horizontal)

# np.append(): Append values to the end of an array
print("\n=== np.append() ===")
original_arr = np.array([1, 2, 3])
appended = np.append(original_arr, [4, 5])
print("Original:", original_arr)
print("After append:", appended)

# np.delete(): Delete elements from an array along a specified axis
print("\n=== np.delete() ===")
full_array = np.array([1, 2, 3, 4, 5])
deleted = np.delete(full_array, 2)  # Delete element at index 2
print("Original:", full_array)
print("After deleting index 2:", deleted)

# np.insert(): Insert values into an array at specified positions
print("\n=== np.insert() ===")
base_array = np.array([1, 2, 3, 5])
inserted = np.insert(base_array, 3, 4)  # Insert 4 at index 3
print("Original:", base_array)
print("After inserting 4 at index 3:", inserted)

# Array indexing and slicing operations
print("\n=== Array Indexing and Slicing ===")
sample_array = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print("Sample array:", sample_array)

# arr[i]: Access an element of an array at index i
print("Element at index 3:", sample_array[3])

# arr[i:j]: Slice an array from index i to j (exclusive)
print("Slice from index 2 to 5:", sample_array[2:5])

# arr[start:end:step]: Slice an array with a step between start and end
print("Slice with step 2:", sample_array[1:8:2])

# arr[:, :]: Access all elements along rows and columns (for 2D arrays)
print("\n=== Multidimensional Array Accessing ===")
multi_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("2D array:\n", multi_array)
print("All rows, column 2:", multi_array[:, 2])
print("Row 1, all columns:", multi_array[1, :])
print("Submatrix (rows 0-1, columns 1-3):\n", multi_array[0:2, 1:3])
