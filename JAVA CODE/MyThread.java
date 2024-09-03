public class MyThread extends Thread {
    public void run() {
        System.out.println("Printing by extending Thread class");
        System.out.println("Hello World");
    }
}

class MyRunnable implements Runnable {
    @Override
    public void run() {
        System.out.println("Printing by using Runnable interface");
        System.out.println("Hello World");
    }
}