s = int(input("Enter size of the array: "))
arr = []
for b in range(s):
        arr.append(int(input(f"Enter the element {b + 1}: ")))
    
r = int(input("Enter the value of K: "))
    
for p in range(s):
        for q in range(p + 1, s):
            if (arr[p] + arr[q]) % r == 0:
                print(f"({arr[p]},{arr[q]})")
