import java.util.Arrays;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class ThreadSleep {
    public static void main(String[] args) throws InterruptedException {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the salaries of five employees: ");
        int[] salaries = new int[5];
        for (int i = 0; i < salaries.length; i++) {
            salaries[i] = sc.nextInt();
        }
        for (int i = 0; i < salaries.length; i++) {
            salaries[i] = (int) (salaries[i] * 1.05);
            TimeUnit.MILLISECONDS.sleep(2000);
        }
        System.out.println("New salaries: " + Arrays.toString(salaries));
        sc.close();
    }
}