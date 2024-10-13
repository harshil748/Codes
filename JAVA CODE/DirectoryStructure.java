import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class DirectoryStructure {
    public static void main(String[] args) {
        try {
            Path documentsDir = Paths.get("Documents");
            Path workDir = documentsDir.resolve("Work");
            Path personalDir = documentsDir.resolve("Personal");
            Files.createDirectories(workDir);
            Files.createDirectories(personalDir);
            Files.createFile(workDir.resolve("project1.txt"));
            Files.createFile(workDir.resolve("project2.txt"));
            Files.createFile(personalDir.resolve("weekendPlan.txt"));
            Files.createFile(personalDir.resolve("summerTrip.txt"));
            System.out.println("Directory structure created successfully.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}