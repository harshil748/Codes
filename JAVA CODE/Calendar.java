import java.util.Scanner;

public class Calendar {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        input.close();
        System.out.println("Enter the month: ");
        int month = input.nextInt();
        System.out.println("Enter the year: ");
        int year = input.nextInt();
        int[] daysInMonth = {31,28,31,30,31,30,31,31,30,31,30,31};
        if (month == 2 && year % 4 == 0) {
            if (year % 100 == 0) {
                if (year % 400 == 0) {
                    daysInMonth[1] = 29;
                }
            } else {
                daysInMonth[1] = 28;
            }
        }
    }
}
/*
 
 */