import java.util.Scanner;

public class AddIntegers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean inputCorrect = true;
        try {
            System.out.print("Enter first integer: ");
            int num1 = Integer.parseInt(sc.nextLine());
            System.out.print("Enter second integer: ");
            int num2 = Integer.parseInt(sc.nextLine());
            int result = num1 + num2;
            System.out.println("The sum of the numbers is: " + result);
        } catch (NumberFormatException e) {
            System.out.println("You did not type an integer!");
            inputCorrect = false;
        }
        if (!inputCorrect) {
            System.out.println("Please enter integers only.");
        }
        sc.close();
    }
}