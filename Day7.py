# stack--->
class stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size#[None,None,None,None]
        self.__top=-1

    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__top==-1):
            return True
        return False

    def push(self,data):#data=5
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1#self.__top=3
            self.__elements[self.__top]=data#5
            #[5,6,7,8]

    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data=self.__elements[self.__top]
            self.__top_=1
            return data
    def display(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            index=self.__top#3
            while(index>=0):
                print(self.__elements[index])
                index-=1

    def get_max_size(self):
        return self.__max_size

ball_stack=stack(4)
print("is it empty",ball_stack.is_empty())
ball_stack.push(5)
print("is it empty",ball_stack.is_empty())
ball_stack.push(6)
ball_stack.push(7)
ball_stack.push(8)
ball_stack.display()
print("size of the stack",ball_stack.get_max_size())
print("The element got deleted",ball_stack.pop())
print("after deleting the element")
ball_stack.display()
print("size of the stack",ball_stack.get_max_size())

#---------------------------------------------------------------------------------------------------------------------
# Queue--->
class queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):#100
        if(self.is_full()):
            print("queue is full!!")
        else:
            self.__rear+=1#4
            self.__elements[self.__rear]=data#100
            #[100,200,300,400,500]
    def dequeue(self):
        if(self.is_empty()):
            print("queue is empty!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size


queue1=queue(4)
print("is it full",queue1.is_full())
print("is it empty",queue1.is_empty())
queue1.enqueue(100)
queue1.display()
queue1.enqueue(200)
queue1.enqueue(300)
queue1.enqueue(400)
queue1.display()
queue1.enqueue(500)
queue1.display()
print("element deleted",queue1.dequeue())
queue1.display()

#---------------------------------------------------------------------------------------------------------------------
def merge_queues(queue1, queue2):
    merged_queue = []

    for i in range(min(len(queue1), len(queue2))):
        merged_queue.append(queue1[i])
        merged_queue.append(queue2[i])

    if len(queue1) > len(queue2):
        merged_queue.extend(queue1[len(queue2):])
    elif len(queue2) > len(queue1):
        merged_queue.extend(queue2[len(queue1):])

    return merged_queue

queue1 = [3, 6, 8]
queue2 = ['b', 'y', 'u', 't', 'r', 'o']
merged_queue = merge_queues(queue1, queue2)
print(merged_queue)

#---------------------------------------------------------------------------------------------------------------------

def merge_list(list1,list2):
    merged_data=""
    list2.reverse()
    for i in range(len(list1)):
        if(list1[i] is None):
            list1[i]=""
        if(list2[i] is None):
            list2[i]=""
        merged_data+=str(list1[i])+str(list2[i])+" "
    return merged_data[:-1]
list1=['T','sk',None,'bl']
list2=['ue','is','y','he']
merged_data=merge_list(list1,list2)
print(merged_data)

#---------------------------------------------------------------------------------------------------------------------


# Traversing a linked list

class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class SlinkedList:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
list=SlinkedList()
list.headval=Node("Mon")



























