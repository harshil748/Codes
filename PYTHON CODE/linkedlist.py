class Node:
    def __init__(ll, data):
        ll.data = data
        ll.next = None

class LinkedList:
    def __init__(ll):
        ll.head = None

    def insert_at_front(ll, data):
        new_node = Node(data)
        new_node.next = ll.head # type: ignore
        ll.head = new_node
        ll.display()

    def delete_at_last(ll):
        if ll.head is None:
            return
        elif ll.head.next is None:
            ll.head = None
        else:
            temp = ll.head
            while temp.next.next is not None: # type: ignore
                temp = temp.next # type: ignore
            temp.next = None # type: ignore
        ll.display()

    def delete_all(ll):
        ll.head = None
        ll.display()

    def display(ll):
        if ll.head is None:
            print("Linked list is empty")
        else:
            temp = ll.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()
linked_list = LinkedList()
linked_list.insert_at_front(3)
linked_list.insert_at_front(2)
linked_list.insert_at_front(1)
linked_list.delete_at_last()
linked_list.delete_at_last()
linked_list.delete_all()