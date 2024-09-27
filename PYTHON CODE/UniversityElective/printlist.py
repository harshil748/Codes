user_list = []
print("Enter elements for the list. Type 'done' when finished.")
while True:
    user_input = input("Enter an element: ")
    if user_input.lower() == "done":
        break
    user_list.append(user_input)
    print("Current list:", user_list)

print("\nFinal list:", user_list)