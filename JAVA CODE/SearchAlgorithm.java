import java.util.Scanner;
import java.util.Arrays;

public class SearchAlgorithm {
    public static void main(String[] args)
    {
        Scanner linear = new Scanner(System.in);
        int size,key;
        System.out.print("Enter size of the array: ");
        size = linear.nextInt();
        int[] arr = new int[size];
        for (int i = 0; i < size; i++) {
            System.out.print("Enter the element " + (i + 1) + " : ");
            arr[i] = linear.nextInt();
        }
        Arrays.sort(arr);
        System.out.println("\nSorted array: ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.print("\nEnter the element to search: ");
        key = linear.nextInt();
        linear.close();
        int linearIndex = linearSearch(arr, key);
        if (linearIndex != -1){
            System.out.println("Element found at index (for linear search): " + linearIndex);
        } else {
            System.out.println("Element not found (for linear search)");
        }
        int binaryIndex = binarySearch(arr, key);
        if (binaryIndex != -1){
            System.out.println("Element found at index (for binary search): " + binaryIndex);
        } else {
            System.out.println("Element not found (for binary search)");
        }
    }
    public static int linearSearch(int[] arr, int key) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == key) {
                return i;
            }
        }
        return -1;
    }
    public static int binarySearch(int[] arr, int key) {
        int left = 0, right = arr.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (arr[mid] == key) {
                return mid;
            } else if (arr[mid] < key) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
}