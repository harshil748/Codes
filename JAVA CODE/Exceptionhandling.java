import java.util.Scanner;
// Java Practical 4.2
class SmallException extends Exception {
    public SmallException(String message) {
        super(message);
    }
}

class BigException extends Exception {
    public BigException(String message) {
        super(message);
    }
}

class OwnException {
    public void printErrorReport(Exception exception) {
        System.out.println("Error: " + exception.getMessage());
    }

    public void testValue(int value) throws SmallException, BigException {
        if (value < 5) {
            throw new SmallException("Value "+value +" is lower than 5");
        } else if (value > 10) {
            throw new BigException("Value "+value +" is higher than 10");
        }
    }
}

public class Exceptionhandling {
    public static void main(String[] args) {
        OwnException ownException = new OwnException();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of test values you want to input:");
        int numberOfValues = scanner.nextInt();
        int[] testValues = new int[numberOfValues];
        System.out.println("Please enter " + numberOfValues + " test values:");
        for (int i = 0; i < numberOfValues; i++) {
            testValues[i] = scanner.nextInt();
        }
        for (int value : testValues) {
            try {
                ownException.testValue(value);
                System.out.println("Value " + value + " is valid.");
            } catch (SmallException | BigException e) {
                ownException.printErrorReport(e);
            }
        }
        scanner.close();
    }
}