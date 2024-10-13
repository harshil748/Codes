abstract class Instrument {
    abstract void play();
    abstract String what();
    abstract void adjust();
}
// Java Practical 3.1
class Wind extends Instrument {
    @Override
    void play() {
        System.out.println("Wind instrument played");
    }

    @Override
    String what() {
        return "Wind";
    }

    @Override
    void adjust() {
        System.out.println("Wind instrument tuned properly");
    }
}

class Percussion extends Instrument {
    @Override
    void play() {
        System.out.println("Percussion instrument played");
    }

    @Override
    String what() {
        return "Percussion";
    }

    @Override
    void adjust() {
        System.out.println("Percussion instrument tuned properly");
    }
}

class Stringed extends Instrument {
    @Override
    void play() {
        System.out.println("Stringed instrument played");
    }

    @Override
    String what() {
        return "Stringed";
    }

    @Override
    void adjust() {
        System.out.println("Stringed instrument tuned properly");
    }
}

class Woodwind extends Wind {
    @Override
    void play() {
        System.out.println("Woodwind instrument played");
    }

    @Override
    String what() {
        return "Woodwind";
    }
}

class Brass extends Wind {
    @Override
    void play() {
        System.out.println("Brass instrument played");
    }

    @Override
    String what() {
        return "Brass";
    }
}

public class Instruments {
    public static void main(String[] args) {
        Instrument[] instruments = {
                new Wind(),
                new Percussion(),
                new Stringed(),
                new Woodwind(),
                new Brass()
        };
        for (Instrument instrument : instruments) {
            System.out.println("Instrument: " + instrument.what());
            instrument.play();
            instrument.adjust();
            System.out.println();
        }
    }
}