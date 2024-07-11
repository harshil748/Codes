public class LinkedList {
    public static void main(String[] args) {
        
    }
    private Node head;
    // Insert a node at the front of the linked list
    public void insertAtFront(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
        display();
    }
    // Delete the last node of the linked list
    public void deleteAtLast() {
        if (head == null) {
            return;
        }
        if (head.next == null) {
            head = null;
            return;
        }
        Node secondLast = head;
        while (secondLast.next.next != null) {
            secondLast = secondLast.next;
        }
        secondLast.next = null;
        display();
    }
    // Delete all nodes of the linked list
    public void deleteAll() {
        head = null;
        display();
    }
    // Display the content of the linked list
    public void display() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }
    // Node class
    private class Node {
        int data;
        Node next;
        Node(int data) {
            this.data = data;
            next = null;
        }
    }
}