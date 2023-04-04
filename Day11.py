#merging two linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def merge_lists(self, list1, list2, n):
        if list1.head is None:
            list1.head = list2.head
            return
        curr_node = list1.head
        count = 1
        while count < n and curr_node is not None:
            curr_node = curr_node.next
            count += 1
        if curr_node is None:
            return
        temp = curr_node.next
        curr_node.next = list2.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = temp

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end="->")
            curr_node = curr_node.next


list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(2)
list1.insert_at_end(4)
list1.insert_at_end(3)
list1.insert_at_end(5)
list2 = LinkedList()
list2.insert_at_end(9)
list2.insert_at_end(8)
list2.insert_at_end(11)
list1.merge_lists(list1, list2, 2)
list1.display()