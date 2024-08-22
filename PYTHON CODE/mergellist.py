class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def mergeTwoLists(self, list1, list2):
        dummyHead = Node(-1)
        curr = dummyHead
        while list1 and list2:
            if list1.data <= list2.data:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        while list1:
            curr.next = list1
            list1 = list1.next
            curr = curr.next

        while list2:
            curr.next = list2
            list2 = list2.next
            curr = curr.next

        return dummyHead.next

    def display(self, llist):
        curr = llist
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()


llist = LinkedList()
llist.list1 = Node(1)
second = Node(3)
third = Node(5)
llist.list1.next = second
second.next = third

llist.list2 = Node(2)
fourth = Node(4)
fifth = Node(6)
llist.list2.next = fourth
fourth.next = fifth
print("Linked List 1:")
llist.display(llist.list1)
print("Linked List 2:")
llist.display(llist.list2)
mergedList = llist.mergeTwoLists(llist.list1, llist.list2)
print("Merged Linked List:")
llist.display(mergedList)
