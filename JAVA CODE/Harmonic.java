import java.util.Scanner;
import harmonic.HarmonicSeries;
// Java Practical 3.4
public class Harmonic {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the value of n: ");
        int n = scanner.nextInt();
        HarmonicSeries harmonicSeries = new HarmonicSeries();
        double sum = harmonicSeries.calculate(n);
        System.out.println("Sum of the harmonic series is: " + sum);
        scanner.close();
    }
}