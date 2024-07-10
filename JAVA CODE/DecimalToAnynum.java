import java.util.Scanner;

public class DecimalToAnynum {
    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        System.out.print("Enter the number: ");
        String number = num.next();
        System.out.print("Enter the base of the number: ");
        int initialbase = num.nextInt();
        System.out.print("Enter the base to convert to: ");
        int basechange = num.nextInt();
        int decimalValue = anyBasetoDecimal(number, initialbase);
        String anybase = decimaltoAnyBase(decimalValue, basechange);
        System.out.println("The number " + number + " in base " + initialbase + " is " + anybase + " and in base "
                + basechange + " is " + decimalValue);
        num.close();
    }

    public static int anyBasetoDecimal(String number, int base) {
        int decimal = 0;
        int length = number.length();
        for (int i = 0; i < length; i++) {
            char digitChar = number.charAt(length - 1 - i);
            int digit;
            if (digitChar >= '0' && digitChar <= '9') {
                digit = digitChar - '0';
            } else {
                digit = digitChar - 'A' + 10;
            }
            decimal += digit * Math.pow(base, i);
        }

        return decimal;
    }

    public static String decimaltoAnyBase(int decimal, int base) {
        if (decimal == 0) {
            return "0";
        }
        StringBuilder result = new StringBuilder();
        while (decimal > 0) {
            int remainder = decimal % base;
            char digitChar;
            if (remainder < 10) {
                digitChar = (char) ('0' + remainder);
            } else {
                digitChar = (char) ('A' + remainder - 10);
            }
            result.insert(0, digitChar);
            decimal /= base;
        }
        return result.toString();
    }
}