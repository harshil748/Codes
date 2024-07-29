import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class Anagrams {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();
        System.out.println("Randomized string: " + getRandom(input));
        System.out.print("Enter another string to check if it is an anagram: ");
        String input2 = scanner.nextLine();
        System.out.println("Is the input an anagram: " + isEqual(input, input2));
        scanner.close();
    }

    public static String getRandom(String s) {
        Random r = new Random();
        char[] arr = s.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            int j = r.nextInt(arr.length);
            char temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        return new String(arr);
    }

    public static boolean isEqual(String s1, String s2) {
        s1 = s1.toLowerCase();
        s2 = s2.toLowerCase();
        char[] arr1 = s1.toCharArray();
        char[] arr2 = s2.toCharArray();
        if (arr1.length != arr2.length) {
            return false;
        }
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        return Arrays.equals(arr1, arr2);
    }
}