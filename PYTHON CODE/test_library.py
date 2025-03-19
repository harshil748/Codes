import unittest
from library.library_manager import LibraryManager


class TestLibraryManager(unittest.TestCase):
    def setUp(self):
        """Initialize a new LibraryManager instance before each test"""
        self.library = LibraryManager()
        # Add some sample books
        self.library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
        self.library.add_book("To Kill a Mockingbird", "Harper Lee")
        self.library.add_book("1984", "George Orwell")

    def test_add_book(self):
        """Test adding a book"""
        self.library.add_book("Brave New World", "Aldous Huxley")
        available_books = self.library.show_books()
        self.assertIn("Brave New World by Aldous Huxley", available_books)

    def test_borrow_book(self):
        """Test borrowing a book"""
        # Borrow an available book
        result = self.library.borrow_book("The Great Gatsby")
        self.assertTrue(result)

        # Check that the book is no longer in available books
        available_books = self.library.show_books()
        self.assertNotIn("The Great Gatsby by F. Scott Fitzgerald", available_books)

    def test_borrow_unavailable_book(self):
        """Test borrowing a book that's already borrowed"""
        # Borrow the book first
        self.library.borrow_book("To Kill a Mockingbird")

        # Try to borrow it again
        result = self.library.borrow_book("To Kill a Mockingbird")
        self.assertFalse(result)

    def test_return_book(self):
        """Test returning a borrowed book"""
        # Borrow a book first
        self.library.borrow_book("1984")

        # Return the book
        result = self.library.return_book("1984")
        self.assertTrue(result)

        # Check that the book is available again
        available_books = self.library.show_books()
        self.assertIn("1984 by George Orwell", available_books)

    def test_return_available_book(self):
        """Test returning a book that wasn't borrowed"""
        # Try to return a book that wasn't borrowed
        result = self.library.return_book("To Kill a Mockingbird")
        self.assertFalse(result)

    def test_show_books(self):
        """Test showing available books"""
        available_books = self.library.show_books()
        expected_books = [
            "The Great Gatsby by F. Scott Fitzgerald",
            "To Kill a Mockingbird by Harper Lee",
            "1984 by George Orwell",
        ]

        # Check that all expected books are in available books
        for book in expected_books:
            self.assertIn(book, available_books)

        # Check that the count is correct
        self.assertEqual(len(available_books), len(expected_books))


if __name__ == "__main__":
    unittest.main()
