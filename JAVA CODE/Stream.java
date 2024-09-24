import java.io.*;
public class Stream {
    public static void main(String[] args) {
        try {
            FileInputStream fis = new FileInputStream("abc.txt");
            FileOutputStream fos = new FileOutputStream("xyz.txt");
            int c;
            while ((c = fis.read()) != -1) {
                fos.write(c);
                System.out.println(c);
            }
            fis.close();
            fos.close();
        } catch (Exception e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}