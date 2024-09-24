import java.io.*;
public class FileHandling {
    public static void main(String[] args) {
        try {
            File obj = new File("filename.txt");
            FileWriter wr = new FileWriter("filename.txt");
            wr.write("Successfully written to the file.");
            wr.close();
            if (obj.createNewFile()) {
                System.out.println("File created: " + obj.getName());
            } else {
                System.out.println("File already exists");
            }
            System.out.println("File Name: " + obj.getName());
            System.out.println("Absolute path: " + obj.getAbsolutePath());
            System.out.println("File exists: " + obj.length());
            System.out.println("File readable: " + obj.canRead());
            System.out.println("File writable: " + obj.canWrite());
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}