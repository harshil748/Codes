strings= ["a", "b", "c"]
integers = ["1", "2", "3"]
mixed = ["a", 1, "b", 2]    
print("a. Original list of flowers:")
print(flowers)
print("\nb. Second element of the list:")
print(flowers[1])
print("\nc. Third element and all elements after:")
print(flowers[2:])
flowers[1] = "Hibiscus"
print("\nd. List after replacing the second element with 'Hibiscus':")
print(flowers)