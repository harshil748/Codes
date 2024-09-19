public class ThreadPriority {
    public static void main(String[] args) {
        Thread dhoni = new Thread(new Player("Dhoni"));
        Thread kohli = new Thread(new Player("Kohli"));
        Thread hardik = new Thread(new Player("Hardik"));
        dhoni.setPriority(Thread.MAX_PRIORITY);
        kohli.setPriority(Thread.NORM_PRIORITY);
        hardik.setPriority(Thread.MIN_PRIORITY);
        dhoni.start();
        kohli.start();
        hardik.start();
    }
}

class Player implements Runnable {
    String name;

    public Player(String name) {
        this.name = name;
    }

    @Override
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println(name + " is running iteration " + i);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}