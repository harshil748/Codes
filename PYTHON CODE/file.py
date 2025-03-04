file_path = "sample.txt"

with open(file_path, 'w') as file:
    file.write("Hello, this is the first line!\n")
    file.write("This is the second line.\n")
    file.write("This is the third and final line.")

with open(file_path, 'r') as file:
    content = file.read()

print(content)

