public class ThreadPriority {
    public static void main(String[] args) throws Exception {
        Thread dhoni = new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println("Dhoni is running");
            }
        }, "Dhoni");
        Thread kohli = new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println("Kohli is running");
            }
        }, "Kohli");
        Thread hardik = new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println("Hardik is running");
            }
        }, "Hardik");
        dhoni.setPriority(Thread.MAX_PRIORITY);
        hardik.setPriority(Thread.MIN_PRIORITY);
        for (int i = 0; i < 5; i++) {
            dhoni.start();
            kohli.start();
            hardik.start();
            dhoni.join();
            kohli.join();
            hardik.join();
            System.out.println("Sleeping for 1000 milliseconds");
            Thread.sleep(1000);
        }
    }
}