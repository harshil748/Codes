import java.util.Scanner;

public class LongestWord {
    public static void main(String[] args) {
        Scanner line = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String sentence = line.nextLine();
        String[] words = sentence.split(" ");
        String longestWord = "";
        int maxLength = 0;
        for (String word : words) {
            if (word.length() > maxLength) {
                maxLength = word.length();
                longestWord = word;
            }
        }
        System.out.println("Longest word's length = " + maxLength);
    }
}