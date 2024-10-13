class Node:
    def __init__(llist, data):
        llist.data = data
        llist.next = None


class LinkedList:
    def __init__(llist): 
        llist.head = None

    def insert_at_first(llist, data): 
        new_node = Node(data)
        new_node.next = llist.head # type: ignore
        llist.head = new_node

    def ispalindrome(llist): 
        slow = llist.head
        fast = llist.head
        while fast and fast.next:
            slow = slow.next # type: ignore
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev # type: ignore
            prev = curr
            curr = next_node

        first_half = llist.head
        while prev and first_half:
            if prev.data != first_half.data:
                return False
            prev = prev.next
            first_half = first_half.next

        return True

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
linked_list.insert_at_first(1)
linked_list.insert_at_first(2)
linked_list.insert_at_first(2)
linked_list.insert_at_first(1)
linked_list.display()
print(linked_list.ispalindrome())