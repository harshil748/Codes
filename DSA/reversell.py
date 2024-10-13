class Node:
    def __init__(llist, data):
        llist.data = data
        llist.next = None

class LinkedList:
    def __init__(llist):
        llist.head = None

    def insert_at_first(llist, data):
        new_node = Node(data)
        new_node.next = llist.head
        llist.head = new_node

    def reverse(llist):
        prev = None
        curr = llist.head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        llist.head = prev
        llist.display()

    def display(llist):
        if llist.head is None:
            print("List is empty")
        else:
            temp = llist.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()

linked_list = LinkedList()
linked_list.insert_at_first(5)
linked_list.insert_at_first(4)
linked_list.insert_at_first(3)
linked_list.insert_at_first(2)
linked_list.insert_at_first(1)
print("Original list:")
linked_list.display()
print("Reversed list:")
linked_list.reverse()