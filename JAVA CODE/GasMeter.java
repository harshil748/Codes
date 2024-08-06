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
}