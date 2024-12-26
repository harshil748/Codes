integers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
floats = (1.1, 2.2, 3.3, 4.4, 5.5)
strings = ("a", "b", "c", "d", "e", "f",)
mixed = ("a", 1, "b", 2.2, "c", 3)
print("Positive index ", integers[1])  
print("Negative index ", integers[-1])
print("Tuple slicing:", integers[1:4])
print("Count of 2 in integer:", integers.count(2))  
print("Index of 'b' in string:", strings.index("b"))
print("Length of integer:", len(integers))  
print("Max of integer:", max(integers))  
print("Min of integer:", min(integers))  
print("Sum of integer:", sum(integers))
def count_distinct(tup):
    distinct = set(tup)
    print("Distinct elements:", distinct)
    print("Count of distinct elements:", len(distinct))

count_distinct(mixed)
sample = [1, 2, 3, 4, 5]
converted = tuple(sample)
print("Converted tuple:", converted)  
converted_list = list(converted)
print("Converted list:", converted_list) 

# unpacked left