import java.util.Scanner;
import java.util.Arrays;
public class SearchAlgorithm {
    public static void main(String[] args)
    {
        Scanner linear = new Scanner(System.in);
        int s;
        System.out.print("Enter size of the array: ");
        s = linear.nextInt();
        int[] arr = new int[s];
        for (int b = 0; b < s; b++) {
            System.out.print("Enter the element " + (b + 1) + " : ");
            arr[b] = linear.nextInt();
        }
        linear.close();
        Arrays.sort(arr);
        System.out.println("\nSorted array: ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        Scanner binary = new Scanner(System.in);
        System.out.print("\nEnter the element to search: ");
        int key = binary.nextInt();
        binary.close();
    }
}
