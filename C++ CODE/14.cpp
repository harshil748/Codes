#include <iostream>
#include <string>
using namespace std;
// Base class for Literature
class Literature
{
protected:
    int id;
    string title;

public:
    Literature(int id, string title) : id(id), title(title) {}
    virtual void displayInfo() = 0;
};
// Derived class for e-Literature
class ELiterature : public Literature
{
protected:
    string doi;

public:
    ELiterature(int id, string title, string doi) : Literature(id, title), doi(doi) {}
    void displayInfo() override
    {
        cout << "ID: " << id << ", Title: " << title << ", DOI: " << doi << endl;
    }
};
// Derived class for hard bound Literature
class HardBoundLiterature : public Literature
{
protected:
    int stock;

public:
    HardBoundLiterature(int id, string title, int stock) : Literature(id, title), stock(stock) {}
    void displayInfo() override
    {
        cout << "ID: " << id << ", Title: " << title << ", Stock: " << stock << endl;
    }
};
// Derived class for Books
class Book : public HardBoundLiterature
{
protected:
    string isbn;

public:
    Book(int id, string title, int stock, string isbn) : HardBoundLiterature(id, title, stock), isbn(isbn) {}
    void displayInfo() override
    {
        cout << "Book - ";
        HardBoundLiterature::displayInfo();
        cout << "ISBN: " << isbn << endl;
    }
};
// Derived class for Magazines
class Magazine : public ELiterature
{
protected:
    string issn;

public:
    Magazine(int id, string title, string doi, string issn) : ELiterature(id, title, doi), issn(issn) {}
    void displayInfo() override
    {
        cout << "Magazine - ";
        ELiterature::displayInfo();
        cout << "ISSN: " << issn << endl;
    }
};
// Library class to manage literature
class Library
{
private:
    static const int MAX_LITERATURE = 100;
    Literature *collection[MAX_LITERATURE];
    int numLiterature;

public:
    Library() : numLiterature(0) {}
    void addLiterature(Literature *l)
    {
        if (numLiterature < MAX_LITERATURE)
        {
            collection[numLiterature++] = l;
        }
        else
        {
            cout << "Library is full, cannot add more literature." << endl;
        }
    }
    void displayAllLiterature()
    {
        for (int i = 0; i < numLiterature; ++i)
        {
            collection[i]->displayInfo();
        }
    }
};
// Function to get user input for book
void inputBook(int &id, string &title, int &stock, string &isbn)
{
    cout << "Enter book ID: ";
    cin >> id;
    cout << "Enter book title: ";
    cin.ignore();
    getline(cin, title);
    cout << "Enter stock: ";
    cin >> stock;
    cout << "Enter ISBN: ";
    cin >> isbn;
}
// Function to get user input for magazine
void inputMagazine(int &id, string &title, string &doi, string &issn)
{
    cout << "Enter magazine ID: ";
    cin >> id;
    cout << "Enter magazine title: ";
    cin.ignore();
    getline(cin, title);
    cout << "Enter DOI: ";
    cin >> doi;
    cout << "Enter ISSN: ";
    cin >> issn;
}
int main()
{
    Library library;
    char choice;
    do
    {
        cout << "Add a literature (B for book, M for magazine, Q to quit): ";
        cin >> choice;
        switch (choice)
        {
        case 'B':
        {
            int id, stock;
            string title, isbn;
            inputBook(id, title, stock, isbn);
            library.addLiterature(new Book(id, title, stock, isbn));
            break;
        }
        case 'M':
        {
            int id;
            string title, doi, issn;
            inputMagazine(id, title, doi, issn);
            library.addLiterature(new Magazine(id, title, doi, issn));
            break;
        }
        case 'Q':
            break;
        default:
            cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 'Q');
    // Display all literature
    library.displayAllLiterature();
    return 0;
}