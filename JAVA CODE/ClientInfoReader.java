import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

class Person {
    String info;

    public Person(String info) {
        this.info = info;
    }

    public String toString() {
        return info;
    }
}

class ClientsInFile {
    public static int readInfo(Person[] people) {
        int count = 0;
        try (BufferedReader br = new BufferedReader(new FileReader("clients.txt"))) {
            String line;
            while ((line = br.readLine()) != null && count < people.length) {
                people[count] = new Person(line);
                count++;
            }
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
        return count;
    }
}

public class ClientInfoReader {
    public static void main(String[] args) {
        Person[] people = new Person[100];
        int count = ClientsInFile.readInfo(people);
        for (int i = 0; i < count; i++) {
            System.out.println(people[i]);
        }
    }
}