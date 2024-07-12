import java.util.Scanner;

public class Practice {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // Prompt user for month and year
        System.out.print("Enter month (1-12): ");
        int month = scanner.nextInt();
        System.out.print("Enter year: ");
        int year = scanner.nextInt();
        // Array of days in each month
        int[] daysInMonth = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        // Adjust for leap year
        if (isLeapYear(year)) {
            daysInMonth[1] = 29;
        }
        // Print the calendar
        printCalendar(month, year, daysInMonth);
        scanner.close();
    }

    // Method to check if a year is a leap year
    public static boolean isLeapYear(int year) {
        if (year % 4 == 0) {
            if (year % 100 == 0) {
                return year % 400 == 0;
            }
            return true;
        }
        return false;
    }

    // Method to calculate the day of the week for the first day of the month
    public static int getFirstDayOfMonth(int month, int year) {
        int y = year - (14 - month) / 12;
        int x = y + y / 4 - y / 100 + y / 400;
        int m = month + 12 * ((14 - month) / 12) - 2;
        return (1 + x + (31 * m) / 12) % 7;
    }

    // Method to print the calendar
    public static void printCalendar(int month, int year, int[] daysInMonth) {
        String[] months = {
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
        };
        String[] daysOfWeek = { "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" };
        System.out.println("    " + months[month - 1] + " " + year);
        for (String day : daysOfWeek) {
            System.out.print(day + " ");
        }
        System.out.println();
        // Get the day of the week of the first day of the month
        int startDay = getFirstDayOfMonth(month, year);
        // Print leading spaces
        for (int i = 0; i < startDay; i++) {
            System.out.print("    ");
        }
        // Print the days of the month
        int daysInCurrentMonth = daysInMonth[month - 1];
        for (int day = 1; day <= daysInCurrentMonth; day++) {
            System.out.printf("%3d ", day);
            if ((day + startDay) % 7 == 0 || day == daysInCurrentMonth) {
                System.out.println();
            }
        }
    }
}