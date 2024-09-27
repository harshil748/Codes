import java.io.*;

public class GradeProcessor {
    public static void main(String[] args) {
        String inputFile = "grades.txt";
        String outputFile = "results.txt";
        try (BufferedReader reader = new BufferedReader(new FileReader(inputFile));
                BufferedWriter writer = new BufferedWriter(new FileWriter(outputFile))) {
            String line;
            while ((line = reader.readLine()) != null) {
                int grade = Integer.parseInt(line.trim());
                int incrementedGrade = (grade < 10) ? grade + 1 : grade;
                writer.write(String.valueOf(incrementedGrade));
                writer.newLine();
                System.out.println(incrementedGrade);
            }
            System.out.println("Grades have been processed and written to " + outputFile);
        } catch (IOException e) {
            System.err.println("An error occurred: " + e.getMessage());
        } catch (NumberFormatException e) {
            System.err.println("Invalid grade format in the input file: " + e.getMessage());
        }
    }
}