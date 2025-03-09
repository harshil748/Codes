strings = ["a", "b", "c"]
integers = [1, 2, 3]
mixed = ["a", 1, "b", 2]
print("First element of strings:", strings[0])
print("Last twi elements of integers:", integers[-2:])
strings[1] = "A"
print("Updated elements:", strings)
integers.append(4)
integers.insert(0, 0)
print("Updated integers:", integers)
popped_value = mixed.pop()
print("Mixed after pop:", mixed)
integers.remove(2)
print("Integers after remove:", integers)
list_concat = strings + ["d", "e"]
print("Concatenated list:", list_concat)
list_repeat = integers * 2
print("Repeated integers:", list_repeat)

square = [i**i for i in range(1,11)]
print("Square:", square)
even_num = [n for n in integers if n % 2 == 0]
print("Even numbers:", even_num)

strings.sort()
print("Sorted strings:", strings)
strings.reverse()
print("Reversed strings:", strings)
strings_copy = strings.copy()
print("Copied strings:", strings_copy)

duplicate = [1, 2, 3, 1, 2, 3]
unique = list(set(duplicate))
print("Unique values:", unique)