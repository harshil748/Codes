class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def is_available(self):
        return self.available
