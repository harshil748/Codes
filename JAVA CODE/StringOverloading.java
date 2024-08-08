import java.util.Scanner;

public class StringOverloading {

    public static void processString(String input) {
        // If the input string has no spaces
        if (!input.contains(" ")) {
            // Replace 'A' with 'Z'
            String modifiedString = input.replace('A', 'Z');
            System.out.println("Modified string: " + modifiedString);
            System.out.println("Length of the string: " + modifiedString.length());
        }
        // If the input string has spaces
        else {
            int midIndex = input.length() / 2;
            String firstHalf = input.substring(0, midIndex);
            String secondHalf = "CHARUSAT";
            String finalString = firstHalf + secondHalf;
            System.out.println("Modified string: " + finalString);
        }
    }

    public static void processString(String input, int maxLength) {
        // If the input string length is more than 10 with spaces
        if (input.length() > 10 && input.contains(" ")) {
            String lowercaseString = input.toLowerCase();
            System.out.println("Modified string: " + lowercaseString);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String inputString = scanner.nextLine();

        processString(inputString);
        processString(inputString, 10);
    }
}