import java.util.Scanner;

public class DecimalToAnynum {
    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        int decimal;
        System.out.print("Enter the number: ");
        decimal = num.nextInt();
        System.out.print("Enter the base: ");
        int base = num.nextInt();
        System.out.println("Enter the base to convert: ");
        int base2 = num.nextInt();
        num.close();
        String deci = anyBasetoDecimal(decimal, base);
        String anybase = decimaltoAnyBase(decimal, base2);
        

    }
    public static String anyBasetoDecimal(int decimal, int base){

       return num; 
    }
    public static String decimaltoAnyBase(int decimal, int base2) {
        return numb;
    }
}
