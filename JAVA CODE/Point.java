public class Point {
    private int x;
    private int y;

    public Point(int x, int y) {
        this.x = stay(x, 0, 100);
        this.y = stay(y, 0, 100);
    }

    public String toString() { 
        return "(" + x + ", " + y + ")";
    }

    public void move(int dx, int dy) { 
        x = stay(x + dx, 0, 100); 
        y = stay(y + dy, 0, 100);
    }

    private int stay(int value, int min, int max) {
        return Math.max(min, Math.min(value, max));
    }

    public class PointTest {
        public static void main(String[] args) {
            Point p1 = new Point(50, 50);
            System.out.println(p1);
            p1.move(30, 40);
            System.out.println(p1);
            p1.move(-90, 20);
            System.out.println(p1);
            p1.move(10, -150);
            System.out.println(p1);
            p1.move(200, 200);
            System.out.println(p1);
        }
    }
}