class MyThread extends Thread {
    public void run() {
        System.out.println("Printing by extending Thread class");
        System.out.println("Hello World");
    }
}
// Java Practical 6.1
class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Printing by using Runnable interface");
        System.out.println("Hello World");
    }
}

public class Threading {
    public static void main(String[] args) {
        MyThread t1 = new MyThread();
        t1.start();
        MyRunnable r = new MyRunnable();
        Thread t2 = new Thread(r);
        t2.start();
    }
}