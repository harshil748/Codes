import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
// Java Practical 7.3
public class OnlineBookstore {
    static HashMap<Integer, Book> books = new HashMap<>();
    static ArrayList<Book> cart = new ArrayList<>();

    public static void main(String[] args) {
        initializeBooks();
        Scanner scanner = new Scanner(System.in);
        boolean running = true;
        while (running) {
            System.out.println("Welcome to the Online Bookstore!");
            System.out.println("1. Browse Books");
            System.out.println("2. Add Book to Cart");
            System.out.println("3. Checkout");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    browseBooks();
                    break;
                case 2:
                    addBookToCart(scanner);
                    break;
                case 3:
                    checkout();
                    break;
                case 4:
                    running = false;
                    break;
                default:
                    System.out.println("Invalid option. Please try again.");
            }
        }
        scanner.close();
    }

    static void initializeBooks() {
        books.put(1, new Book("1984", "George Orwell", 9.99));
        books.put(2, new Book("To Kill a Mockingbird", "Harper Lee", 7.99));
        books.put(3, new Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99));
    }

    static void browseBooks() {
        System.out.println("Available Books:");
        for (Map.Entry<Integer, Book> entry : books.entrySet()) {
            System.out.println(entry.getKey() + ". " + entry.getValue());
        }
    }

    static void addBookToCart(Scanner scanner) {
        System.out.print("Enter the book ID to add to cart: ");
        int bookId = scanner.nextInt();
        if (books.containsKey(bookId)) {
            cart.add(books.get(bookId));
            System.out.println("Book added to cart.");
        } else {
            System.out.println("Book ID not found.");
        }
    }

    static void checkout() {
        double total = 0;
        System.out.println("Items in your cart:");
        for (Book book : cart) {
            System.out.println(book);
            total += book.getPrice();
        }
        System.out.printf("Total cost: $%.2f%n", total);
        cart.clear();
    }
}

class Book {
    String title;
    String author;
    double price;

    public Book(String title, String author, double price) {
        this.title = title;
        this.author = author;
        this.price = price;
    }

    public double getPrice() {
        return price;
    }

    @Override
    public String toString() {
        return title + " by " + author + " - $" + price;
    }
}