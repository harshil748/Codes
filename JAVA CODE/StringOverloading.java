import java.util.Scanner;

public class StringOverloading {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String inputString = scanner.nextLine();

        if (inputString.contains(" ")) {
            if (inputString.length() > 10) {
                processString(inputString);
            } else {
                processStringWithSpace(inputString);
            }
        } else {
            processStringWithoutSpace(inputString);
        }
        scanner.close();
    }

    public static void processStringWithoutSpace(String str) {
        String modifiedString = str.replace('A', 'Z');
        System.out.println("Modified string: " + modifiedString);
        System.out.println("Length of the string: " + str.length());
    }

    public static void processStringWithSpace(String str) {
        String[] parts = str.split(" ");
        String firstHalf = parts[0];
        String secondHalf = "CHARUSAT";
        String modifiedString = firstHalf + " " + secondHalf;
        System.out.println("Modified string: " + modifiedString);
    }

    public static void processString(String str) {
        String modifiedString = str.toLowerCase();
        System.out.println("Modified string: " + modifiedString);
    }
}