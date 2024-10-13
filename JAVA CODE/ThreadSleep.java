import java.util.Scanner;
// Java Practical 6.2
public class ThreadSleep {
    public static void main(String[] args) {
        double[] salaries = new double[5];
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < salaries.length; i++) {
            System.out.print("Enter salary for employee " + (i + 1) + ": ");
            salaries[i] = scanner.nextDouble();
        }
        Thread incrementThread = new Thread(() -> {
            for (int i = 0; i < salaries.length; i++) {
                salaries[i] += salaries[i] * 0.05;
                System.out.println("New salary of employee " + (i + 1) + ": " + salaries[i]);
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    System.out.println("Thread interrupted: " + e.getMessage());
                }
            }
        });
        incrementThread.start();
        scanner.close();
    }
}