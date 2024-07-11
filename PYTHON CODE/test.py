class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.display()

    def delete_at_last(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
        self.display()

    def delete_all(self):
        self.head = None
        self.display()

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()

# Test the implementation
linked_list = LinkedList()

linked_list.insert_at_front(3)
linked_list.insert_at_front(2)
linked_list.insert_at_front(1)

linked_list.delete_at_last()

linked_list.delete_all()