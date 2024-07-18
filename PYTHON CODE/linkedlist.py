class Node:
    def __init__(llist, data):
        llist.data = data
        llist.next = None


class LinkedList:
    def __init__(llist):
        llist.head = None

    def insertatfirst(llist, data):
        new_node = Node(data)
        new_node.next = llist.head 
        llist.head = new_node
        llist.display()

    def deleteatlast(llist):
        if llist.head is None:
            return
        if llist.head.next is None:
            llist.head = None
            return
        temp = llist.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        llist.display()

    def deleteall(llist):
        llist.head = None
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
linked_list.insertatfirst(3) 
linked_list.insertatfirst(2)
linked_list.insertatfirst(1)
linked_list.deleteatlast()
linked_list.deleteall()