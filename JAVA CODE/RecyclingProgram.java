import java.util.Scanner;

interface Recyclable {
    void recycle();

    default void Input() {
        System.out.println("Give proper input");
    }
}

class Fabric implements Recyclable {
    @Override
    public void recycle() {
        System.out.println("Fabric recycled...");
    }

    @Override
    public String toString() {
        return "Fabric";
    }
}

class Bottle implements Recyclable {
    @Override
    public void recycle() {
        System.out.println("Bottle recycled...");
    }

    @Override
    public String toString() {
        return "Bottle";
    }
}

class Paper implements Recyclable {
    @Override
    public void recycle() {
        System.out.println("Paper recycled...");
    }

    @Override
    public String toString() {
        return "Paper";
    }
}

public class RecyclingProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Recyclable[] recyclables = { new Fabric(),
                new Bottle(),
                new Paper()
        };
        while (true) {
            System.out.println("What do you want to recycle? Choose a number.");
            System.out.println("1 - Clothes");
            System.out.println("2 - Bottles");
            System.out.println("3 - Newspapers");
            System.out.println("4 - Exit");
            System.out.print("Choose a Number: ");
            int choice = scanner.nextInt();
            if (choice == 4) {
                System.out.println("Thanks for coming...");
                break;
            } else if (choice >= 1 && choice <= 3) {
                recyclables[choice - 1].recycle();
            } else {
                recyclables[0].Input();
            }
        }
        scanner.close();
    }
}