import java.util.Scanner;

public class Calendar {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the month: ");
        int month = input.nextInt();
        System.out.println("Enter the year: ");
        int year = input.nextInt();
        int[] daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if (isLeapYear(year)) {
            daysInMonth[1] = 29;
        }
        displayCalendar(month, year, daysInMonth);
        input.close();
    }

    public static void displayCalendar(int month, int year, int[] daysInMonth) {
        String[] months = { "January", "February", "March", "April", "May", "June", "July", "August", "September",
                "October", "November", "December" };
        String[] daysOfWeek = { "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" };
        System.out.println("    " + months[month - 1] + " " + year);
        for (String day : daysOfWeek) {
            System.out.print(day + " ");
        }
        System.out.println();
        int firstDay = getFirstDayOfMonth(month, year);
        for (int i = 0; i < firstDay; i++) {
            System.out.print("    ");
        }
        int daysInCurrentMonth = daysInMonth[month - 1];
        for (int day = 1; day <= daysInCurrentMonth; day++) {
            System.out.printf("%4d", day);
            if ((day + firstDay) % 7 == 0 || day == daysInCurrentMonth) {
                System.out.println();
            }
        }
    }

    public static boolean isLeapYear(int year) {
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    }

    public static int getFirstDayOfMonth(int month, int year) {
        int y = year - (14 - month) / 12;
        int x = y + y / 4 - y / 100 + y / 400;
        int m = month + 12 * ((14 - month) / 12) - 2;
        return (1 + x + (31 * m) / 12) % 7;
    }
}