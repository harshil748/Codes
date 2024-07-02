import java.util.Scanner;

public class MobileNumberParser {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a mobile number: ");
        String mobileNumber = scanner.nextLine();
        parseMobileNumber(mobileNumber);
        scanner.close();
    }

    public static void parseMobileNumber(String mobileNumber) {
        mobileNumber = mobileNumber.replace(" ", "").replace("-", "");
        if (mobileNumber.startsWith("+91")) {
            String operatorCode = mobileNumber.substring(3, 5);
            String switchingCode = mobileNumber.substring(5, 8);
            String uniqueCode = mobileNumber.substring(8, 13);
            System.out.println("Mobile system operator code is " + operatorCode);
            System.out.println("MSC is " + switchingCode);
            System.out.println("Unique code is " + uniqueCode);
        } else {
            System.out.println("Invalid mobile number format. Please enter a number in '+91-AA-BBB-CCCCC' format.");
        }
    }
}