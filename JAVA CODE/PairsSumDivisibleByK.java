import java.util.Scanner;

public class PairsSumDivisibleByK {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int s, r;
        System.out.print("Enter size of the array: ");
        s = scanner.nextInt();
        int[] arr = new int[s];
        for (int b = 0; b < s; b++) {
            System.out.print("Enter the element" + (b + 1) + " : ");
            arr[b] = scanner.nextInt();
        }
        System.out.print("Enter the value of k: ");
        r = scanner.nextInt();
        for (int p = 0; p < s; p++) {
            for (int q = p + 1; q < s; q++) {
                if ((arr[p] + arr[q]) % r == 0) {
                    System.out.println("(" + arr[p] + "," + arr[q] + ")");
                }
            }
        }
        scanner.close();
    }
}