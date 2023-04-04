#traversing a linked list

class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class Slinkedlist:
    def __init__(self):
        self.headval=None
   # print the linked list
    def ListPrint(self):
        printval=self.headval #1000
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval

    def Atbegining(self,newdata):
        NewNode=Node(newdata)
        #update the new nodes next val to existing node
        NewNode.nextval=self.headval
        self.headval=NewNode

    #function to add new node
    def AtEnd(self,newdata): #"Thu"
        NewNode=Node(newdata)#5000
        if self.headval is None:
            self.headval=NewNode
            return
        laste = self.headval #laste = 1000
        while(laste.nextval): #3000
            laste =laste.nextval #3000
        laste.nextval=NewNode

    # function to add node inbetween
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode=Node(newdata)
        NewNode.nextval=middle_node.nextval
        middle_node.nextval=NewNode



list=Slinkedlist()
list.headval=Node("Mon") #1000
e2=Node("Tue") #2000
e3=Node("Wed") #3000

#link first Node to second Node
list.headval.nextval=e2

#link second node to third node
e2.nextval=e3
list.Atbegining("sun")
list.AtEnd("Thu")
list.Inbetween(list.headval.nextval.nextval.nextval.nextval,"Fri")
list.ListPrint()

# # --------------------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node=None
    def traverse_list(self):
        if self.start_node is None:
            print("list has no element")
            return
        else:
            n=self.start_node
            while n is not None:
                print(n.item," ")
                n=n.ref
    def insert_at_start(self,data):
        new_node =Node(data)
        new_node.ref=self.start_node
        self.start_node=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.start_node is None:
            self.start_node=new_node
            return
        n=self.start_node
        while n.ref is not None:
            n=n.ref
        n.ref=new_node

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        self.start_node=self.start_node.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        n=self.start_node
        while n.ref.ref is not None:
            n= n.ref
        n.ref= None

    def delete_element_by_value(self,x):
        if self.start_node is None:
            print("The list has no elements to delete")
            return
        if self.start_node.item==x:
            self.start_node=self.start_node.ref
            return

        n=self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n=n.ref

        if n.ref is None:
            print("item not found in the list")
        else:
            n.ref=n.ref.ref

    def search_item(self,x):
        if self.start_node is None:
            print("List has no elements")
            return
        n=self.start_node
        while n is not None:
            if n.item ==x:
                print("Item found")
                return True
            n=n.ref
        print("item not found")
        return False

    def get_count(self):
        if self.start_node is None:
            return 0
        n=self.start_node
        count=0
        while n is not None:
            count=count+1
            n=n.ref
        return count

    def insert_at_index(self,index,data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node=new_node
        i=1
        n=self.start_node
        while i<index-1 and n is not None:
            n=n.ref
            i=i+1
        if n is None:
            print("Index out of bound")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref = new_node


new_linked_list=LinkedList()
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)
new_linked_list.insert_at_end(20)
new_linked_list.insert_at_end(25)
new_linked_list.insert_at_end(30)
new_linked_list.insert_at_end(35)
new_linked_list.insert_at_end(40)
new_linked_list.insert_at_end(45)
new_linked_list.traverse_list()
new_linked_list.delete_at_start()

print("after deletion at the begining")
new_linked_list.traverse_list()
new_linked_list.delete_at_end()
print("after deletion at the end")
new_linked_list.traverse_list()
new_linked_list.delete_element_by_value(20)
print("after deleting 30")
new_linked_list.traverse_list()
new_linked_list.search_item(5)
new_linked_list.search_item(25)
print("the number of Nodes",new_linked_list.get_count())
new_linked_list.insert_at_index(3,8)
new_linked_list.traverse_list()