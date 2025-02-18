class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def avg_grade(self):
        return sum(self.grade) / len(self.grade)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grades:", self.grade)
        print("Average Grade:", self.avg_grade())


name = input("Enter the student's name: ")
age = int(input("Enter the student's age: "))
grades = list(map(int, input("Enter grades : ").split()))
student = Student(name, age, grades)
student.display()