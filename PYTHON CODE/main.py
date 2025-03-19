from library.library_manager import LibraryManager


def main():
    library = LibraryManager()
    n = int(input())
    for _ in range(n):
        line = input().strip()
        parts = line.split()
        if len(parts) < 3:
            continue

        author = " ".join(parts[-2:])
        title = " ".join(parts[:-2])
        library.add_book(title, author)
    while True:
        try:
            transaction = input().strip()
            if not transaction:
                break

            action, title = transaction[0], transaction[2:]

            if action == "B":
                if library.borrow_book(title):
                    print(f"{title} borrowed!")
                else:
                    print("Book not available!")
            elif action == "R":
                if library.return_book(title):
                    print("Book returned!")
                else:
                    print("Invalid return request!")
        except EOFError:
            break

    print("Available books:")
    available_books = library.show_books()
    for book in available_books:
        print(book)