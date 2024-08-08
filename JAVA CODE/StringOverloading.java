import java.util.Scanner;

public class StringOverloading {

    public static void processString(String input) {
        if (!input.contains(" ")) {
            String modifiedString = input.replace('A', 'Z');
            System.out.println("Modified string: " + modifiedString);
            System.out.println("Length of the string: " + modifiedString.length());
        } else {
            int midIndex = input.length() / 2;
            String firstHalf = input.substring(0, midIndex);
            String secondHalf = "CHARUSAT";
            String finalString = firstHalf + secondHalf;
            System.out.println("Modified string: " + finalString);
        }
    }

    public static void processString(String input, int maxLength) {
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
        scanner.close();
    }
}