import java.util.Scanner;
// Java Practical 3.3
public class BottleSoda {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Type in the name of the soda: ");
        String name = scanner.nextLine();
        System.out.print("Type in the volume of the bottle: ");
        double volume = scanner.nextDouble();
        SodaBottle sodaBottle = new SodaBottle(name, volume);
        System.out.println(sodaBottle);
        sodaBottle.recycle();
        scanner.close();
    }
}

class Botle {
    protected double volume;

    public Botle(double volume) {
        this.volume = volume;
    }

    public double returnVolume() {
        return volume;
    }
}

interface Recyclble {
    void recycle();
}

class SodaBottle extends Botle implements Recyclble {
    private String name;

    public SodaBottle(String name, double volume) {
        super(volume);
        this.name = name;
    }

    @Override
    public String toString() {
        return name + ", " + volume + " litres";
    }

    @Override
    public void recycle() {
        System.out.println("Bottle returned for recycling.");
    }
}