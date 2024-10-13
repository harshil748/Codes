import java.util.ArrayList;
import java.util.Collections;
// Java Practical 7.2
class Card {
    String suit;
    String rank;

    public Card(String suit, String rank) {
        this.suit = suit;
        this.rank = rank;
    }

    @Override
    public String toString() {
        return rank + " of " + suit;
    }
}

class Deck {
    private ArrayList<Card> cards;

    public Deck() {
        cards = new ArrayList<>();
        String[] suits = { "Hearts", "Diamonds", "Clubs", "Spades" };
        String[] ranks = { "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace" };
        for (String suit : suits) {
            for (String rank : ranks) {
                cards.add(new Card(suit, rank));
            }
        }
    }

    public void shuffle() {
        Collections.shuffle(cards);
    }

    public void displayCards() {
        for (Card card : cards) {
            System.out.println(card);
        }
    }
}

public class CardDeck {
    public static void main(String[] args) {
        Deck deck = new Deck();
        deck.shuffle();
        deck.displayCards();
    }
}