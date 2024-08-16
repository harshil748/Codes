def check_number(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
        
user_input = int(input("Enter a number: "))
check_number(user_input)