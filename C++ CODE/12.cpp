#include <iostream>
#include <string>
#include <iomanip>
using namespace std;
class Student
{
public:
    string studentID, studentName;
    int semester;
    float theoryMarks[3], practicalMarks[3], totalCredits = 3 * 3, sgpa = 0.0;
    string subjectNames[3];
    void getStudentDetails()
    {
        cout << "Enter Student ID: ";
        cin >> studentID;
        cout << "Enter Student Name: ";
        cin.ignore();
        getline(cin, studentName);
        cout << "Enter Semester: ";
        cin >> semester;
        for (int i = 0; i < 3; i++)
        {
            cout << "Enter Subject Name for Subject " << i + 1 << ": ";
            cin.ignore();
            getline(cin, subjectNames[i]);
            cout << "Enter Theory Marks for Subject " << i + 1 << ": ";
            cin >> theoryMarks[i];
            cout << "Enter Practical Marks for Subject " << i + 1 << ": ";
            cin >> practicalMarks[i];
        }
    }   
    string calculateLetterGrade(int marks)
    {
        if (marks >= 80)
            return "AA";
        else if (marks >= 73)
            return "AB";
        else if (marks >= 66)
            return "BB";
        else if (marks >= 60)
            return "BC";
        else if (marks >= 55)
            return "CC";
        else if (marks >= 50)
            return "CD";
        else if (marks >= 45)
            return "DD";
        else
            return "FF";
    }
    float calculateGradePoint(string letterGrade)
    {
        if (letterGrade == "AA")
            return 10.0;
        else if (letterGrade == "AB")
            return 9.0;
        else if (letterGrade == "BB")
            return 8.0;
        else if (letterGrade == "BC")
            return 7.0;
        else if (letterGrade == "CC")
            return 6.0;
        else if (letterGrade == "CD")
            return 5.0;
        else if (letterGrade == "DD")
            return 4.0;
        else
            return 0.0;
    }
    void calculateSGPA()
    {
        float totalGradePoints = 0.0;
        for (int i = 0; i < 3; i++)
        {
            totalGradePoints += calculateGradePoint(calculateLetterGrade(theoryMarks[i] + practicalMarks[i]));
        }
        sgpa = totalGradePoints / totalCredits;
    }
    void displayStudentDetails()
    {
        cout << "Student ID: " << studentID << endl;
        cout << "Student Name: " << studentName << endl;
        cout << "Semester: " << semester << endl;
        for (int i = 0; i < 3; i++)
        {
            cout << left << setw(20) << subjectNames[i] << setw(15) << theoryMarks[i] << setw(15) << practicalMarks[i] << setw(15) << calculateLetterGrade(theoryMarks[i] + practicalMarks[i]) << endl;
        }
    }
    void displaySGPA()
    {
        cout << "SGPA: " << sgpa << endl;
    }
};
int main()
{
    Student student;
    student.getStudentDetails();
    student.displayStudentDetails();
    student.calculateSGPA();
    student.displaySGPA();
    return 0;
}