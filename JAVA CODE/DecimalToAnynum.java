import java.util.Scanner;

public class DecimalToAnynum {
    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        System.out.print("Enter the number: ");
        String number = num.next();
        System.out.print("Enter the base of the number: ");
        int initialbase = num.nextInt();
        System.out.println("Enter the base to convert to: ");
        int basechange = num.nextInt();
        int decimalValue = anyBasetoDecimal(number, initialbase);
        
        String anybase = decimaltoAnyBase(decimalValue, basechange);
        num.close();
    }
    public static String anyBasetoDecimal(int decimal, int base){
        int decimal = 0;
        int length = number.length();
        for (int i = 0; i < length - 1; i++){

        }

       return num; 
    }
    public static String decimaltoAnyBase(int decimal, int base2) {
        return result.toString();
    }
}
