import java.io.*;

public class FileHandling {
    void createFile() {
        try {
            File obj = new File("C:\\Users\\User\\Desktop\\Java\\JAVA CODE\\files\\filename.txt");
            if (obj.createNewFile()) {
                System.out.println("File created: " + obj.getName());
            } else {
                System.out.println("File already exists");
            }
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

    }
}
