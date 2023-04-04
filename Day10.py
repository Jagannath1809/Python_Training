#Linear Search in python
def LinerSearch(array,n,x):
    #Going through the array sequentially
    for i in range(0,n):
        if (array[i]==x):
            return i
    return -1
array=[2,4,0,1,9]
x=9#key
n=len(array)
result=LinerSearch(array,n,x)
if (result==-1):
    print("Element not found")
else:
    print("Element found at index: ",result)

# --------------------------------------------------------------------------------------------------------------------
# Binary Search in python
def BinarySearch(array,x,low,high):
    # Repeat untill the pointer low and high meet each other
    while low<=high:
        mid=low + (high - low)//2
        if array[mid]==x:
            return  mid
        elif array[mid]<x:
            low = mid+1
        else:
            high = mid-1
    return -1
array=[3,4,5,6,7,8,9]
x=10
result = BinarySearch(array,x,0,len(array)-1)
if result!=-1:
    print("Element found at the index: ",str(result))
else:
    print("Not Found")

# --------------------------------------------------------------------------------------------------------------------
class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val=item
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + "->", end='')
        inorder(root.right)
def postOredr(root):
    if root:
        postOredr(root.left)
        postOredr(root.right)
        print(str(root.val)+"->",end='')
def preOrder(root):
    if root:
        # traverse Root
        print(str(root.val)+"->",end='')
        # traverse left
        preOrder(root.left)
        # traverse right
        preOrder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("In order Traversal.")
inorder(root)
print("\npost order Traversal.")
postOredr(root)
print("\npre order Traversal.")
preOrder(root)


# --------------------------------------------------------------------------------------------------------------------
# Binary search tree operation in python
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->", end=' ')
        inorder(root.right)

# insert a node
def insert(node,key):
    # return a new node if the tree is empty
    if node is None:
        return Node(key)
    # traverse to the right place and insert the node
    if key < node.key:
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right,key)
    return node

# find the inorderSuccessor
def minvalueNode(node):
    current=node
    # find the leftmost leaf
    while(current.left is not None):
        current = current.left
    return current

# Deleting Node
def deleteNode(root,key):
    if root is not None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left,key)
    elif key > root.key:
        root.right = deleteNode(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root - None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minvalueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right,temp.key)
    return root

root = None
root = insert(root,8)
root = insert(root,3)
root = insert(root,1)
root = insert(root,6)
root = insert(root,7)
root = insert(root,10)
root = insert(root,14)
root = insert(root,4)
print("Inorder Traversal: ",end='')
inorder(root)
print("\nafter deleting: ")
root = deleteNode(root,6)
print("\nInorder Traversal: ",end='')
inorder(root)
# --------------------------------------------------------------------------------------------------------------------

def check_double(list1,list2):
    new_list=[]
    for i in list1:
        if(2*i in list2):
            new_list.append(i)
    return new_list
list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34]
print(check_double(list1,list2))

# --------------------------------------------------------------------------------------------------------------------

class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.headval = None

    def listprint(self):
        temp = self.headval
        while temp is not None:
            print(temp.data.comp_name, temp.data.t_seat, temp.data.n_pass)
            print()
            temp = temp.next

    def athead(self, data):
        newnode = node(data)
        if (self.headval == None):
            self.headval = newnode
        else:
            newnode.next = self.headval
            self.headval = newnode

    def atend(self, data):
        newnode = node(data)
        if (self.headval == None):
            self.headval = newnode
        else:
            temp = self.headval
            while (temp.next != None):
                temp = temp.next
            temp.next = newnode

    def len(self):
        cnt = 0
        temp = self.headval
        while temp is not None:
            cnt += 1
            temp = temp.next
        print(cnt)


class train:
    def __init__(self, tname, c_list):
        self.tname = tname
        self.c_list = c_list

    def get_train_name(self):
        return self.tname

    def get_compartment(self):
        self.c_list.listprint()

    def count_compartment(self):
        self.c_list.len()

    def check_vacancy(self):
        temp = self.c_list.headval
        cnt = 0
        while temp is not None:
            if (temp.data.t_seat - temp.data.n_pass >= temp.data.t_seat // 2):
                cnt += 1
            temp = temp.next
        print(cnt)


class Compartment:
    def __init__(self, comp_name, n_pass, t_seat):
        self.comp_name = comp_name
        self.t_seat = t_seat
        self.n_pass = n_pass


list = linkedlist()
c1 = Compartment("SL", 250, 400)
c2 = Compartment("2AC", 125, 280)
c3 = Compartment("3AC", 120, 300)
c4 = Compartment("FC", 160, 300)
c5 = Compartment("1AC", 100, 210)
list.atend(c1)
list.atend(c2)
list.atend(c3)
list.atend(c4)
list.atend(c5)

t1 = train("Rajadhani", list)
t1.count_compartment()
t1.check_vacancy()
t1.get_compartment()
print(t1.get_train_name())






























