import java.util.Scanner;

public class MorseCodeConverter {
    public static void main(String[] args) {
        String[] letters = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};
        String[] morseCodes = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};

        Scanner scanner = new Scanner(System.in);

        int choice;
        do {
            System.out.println("Enter 1 for String to Morse code conversion");
            System.out.println("Enter 2 for Morse code to String conversion");
            System.out.println("Enter 3 to Exit");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Enter a string:");
                    scanner.nextLine(); // Consume the newline character
                    String inputString = scanner.nextLine().toUpperCase();
                    String morseCode = convertToMorseCode(inputString, letters, morseCodes);
                    System.out.println("Morse code: " + morseCode);
                    break;
                case 2:
                    System.out.println("Enter Morse code:");
                    scanner.nextLine(); // Consume the newline character
                    String inputMorseCode = scanner.nextLine();
                    String string = convertToString(inputMorseCode, letters, morseCodes);
                    System.out.println("String: " + string);
                    break;
                case 3:
                    System.out.println("Thank you for using Morse Code Converter!");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        } while (choice != 3);

        scanner.close();
    }

    public static String convertToMorseCode(String inputString, String[] letters, String[] morseCodes) {
        StringBuilder morseCode = new StringBuilder();
        for (int i = 0; i < inputString.length(); i++) {
            char c = inputString.charAt(i);
            if (Character.isLetter(c)) {
                int index = c - 'A';
                morseCode.append(morseCodes[index]).append(" ");
            }
        }
        return morseCode.toString().trim();
    }

    public static String convertToString(String inputMorseCode, String[] letters, String[] morseCodes) {
        StringBuilder string = new StringBuilder();
        String[] codes = inputMorseCode.split(" ");
        for (String code : codes) {
            for (int i = 0; i < morseCodes.length; i++) {
                if (code.equals(morseCodes[i])) {
                    string.append(letters[i]);
                    break;
                }
            }
        }
        return string.toString();
    }
}