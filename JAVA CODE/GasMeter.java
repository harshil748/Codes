import java.util.Scanner;

public class GasMeter {
    private static double octane95 = 0.0;
    private static double octane98 = 0.0;
    private static double diesel = 0.0;

    public static void refuel(int type, String amount) {
        double refuelam = Double.parseDouble(amount);
        switch (type) {
            case 1:
                octane95 += refuelam;
                break;
            case 2:
                octane98 += refuelam;
                break;
            case 3:
                diesel += refuelam;
                break;
        }
    }
    public static double total() {
        return octane95 + octane98 + diesel;
    }
    public static double total95() {
        return octane95;
    }
    public static double total98() {
        return octane98;
    }
    public static double totalD() {
        return diesel;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(true){
            System.out.println("what do you want: 1=95, 2=98, 3=Diesel (type any other number to quit): ");
            int choice = sc.nextInt();
            if (choice < 1 || choice > 3) {
                break;
            }
            System.out.println("How much do you want to refuel: ");
            String amount = sc.next();
            refuel(choice, amount);
        }
        sc.close();
        System.out.println("Total refueled: " + total());
        System.out.println("Total refueled 95 Octane: " + total95());
        System.out.println("Total refueled 98 Octane: " + total98());
        System.out.println("Total refueled Diesel: " + totalD());
    }
}