from .book import Book


class LibraryManager:
    def __init__(self):
        self.books = {} 

    def add_book(self, title, author):
        self.books[title] = Book(title, author)

    def borrow_book(self, title):
        if title in self.books and self.books[title].is_available():
            self.books[title].available = False
            return True
        return False

    def return_book(self, title):
        if title in self.books and not self.books[title].is_available():
            self.books[title].available = True
            return True
        return False

    def show_books(self):
        available_books = []
        for title, book in self.books.items():
            if book.is_available():
                available_books.append(f"{title} by {book.author}")
        return available_books