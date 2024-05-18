#include <iostream>
#include <iomanip>
#include <string>
using namespace std;
string calculateLetterGrade(int marks) // function to calculate letter grade
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

int main()
{
    string studentID, studentName;
    int semester;
    float theoryMarks[3], practicalMarks[3], totalCredits = 3 * 3, sgpa = 0.0;
    string subjectNames[3];
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
        cout << "Enter Theory Marks for " << subjectNames[i] << ": ";
        cin >> theoryMarks[i];
        cout << "Enter Practical Marks for " << subjectNames[i] << ": ";
        cin >> practicalMarks[i];
    }
    cout << "\nStudent ID: " << studentID;
    cout << "\nStudent Name: " << studentName;
    cout << "\nSemester: " << semester;
    cout << "\n\nSubject\t\tTheory\t\tPractical\tLetter Grade" << endl;
    for (int i = 0; i < 3; i++)
    {
        cout << left << setw(20) << subjectNames[i] << setw(15) << theoryMarks[i] << setw(15) << practicalMarks[i] << setw(15) << calculateLetterGrade(theoryMarks[i] + practicalMarks[i]) << endl;
    }
    for (int i = 0; i < 3; i++)
    {
        sgpa += 3 * (calculateGradePoint(calculateLetterGrade(theoryMarks[i])) + calculateGradePoint(calculateLetterGrade(practicalMarks[i]))) / 2;
    }
    sgpa /= totalCredits;
    cout << "\nSGPA: " << fixed << setprecision(2) << sgpa << endl;
    return 0;
}