class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Student ID:", self.student_id)


name = input("Enter name: ")
age = int(input("Enter age: "))
student_id = input("Enter student ID: ")
student = Student(name, age, student_id)
student.display_info()
