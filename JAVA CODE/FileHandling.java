import java.io.*;
import java.util.Scanner;
public class FileHandling {
    public static void main(String[] args) {
        try {
            File obj = new File("filename.txt");
            FileWriter wr = new FileWriter("filename.txt");
            Scanner sc = new Scanner(System.in);
            FileReader fr = new FileReader("filename.txt");
            wr.write("Successfully written to the file.");
            wr.close();
            while (sc.hasNextLine()) {
                String str = sc.nextLine();
                wr.write(str);
            }
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