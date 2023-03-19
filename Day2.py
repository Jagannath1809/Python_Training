#list
list1=[]
print(list1,type(list1))
list2=[10,20,30,40]
print(list2,type(list2))
list3=[10,20.2,30+3j,True,"python"]
print(list3,type(list3))
list4=list([100,200,300])
print(list4,type(list4))
list5=[101,201,301,401]
print(list5,type(list5))
list5.append(501)
print(list5,type(list5))
list5.extend([601,701,801])
print(list5,type(list5))
list5.insert(0,51)
print(list5,type(list5))
list5.insert(4,350)
print(list5,type(list5))
list5.remove(801)
print(list5,type(list5))
list5.pop(0)
print(list5,type(list5))
del list5[1]
print(list5,type(list5))

# ------------------------------------------------------------------------------------------

#letters and digits counter

def function1(str1):
    l_count=0
    d_count=0
    for i in str1:
        if i.isalpha():
            l_count+=1
        elif i.isdigit():
            d_count+=1
        else:
            continue
    return [l_count,d_count]
str1=input()
print(function1(str1))

# ------------------------------------------------------------------------------------------

# ocuurance counter
def find(num_list,n):
    count=0
    for x in num_list:
        index=num_list.index(x)+1
        for y in range(index,len(num_list)):
            if x+num_list[y]==n:
                count+=1
    return count
num_list=[1,2,7,4,5,6,0,3]
n=6
print(find(num_list,n))

# ------------------------------------------------------------------------------------------

# string slicing

def new(str):
    length=len(str)
    if length<2:
        return(-1)
    elif length==2:
        return (str*2)
    else:
        return (str[0:2]+str[-2:])
str=input()
print(new(str))

# ------------------------------------------------------------------------------------------
def change(str):
    length=len(str)
    if length > 2:
        if(str[-3:]=="ing"):
            str+="ly"
        else:
            str+="ing"
    return str
str=input()
print(change(str))

# ------------------------------------------------------------------------------------------


def check_double(n):
    double=int(n)*2
    length=len(n)
    d_length=len(str(double))
    if(length==d_length):
        for i in n:
            if i in str(double):
                print(i)
            else:
                return False

n=input()
print(check_double(n))

# ------------------------------------------------------------------------------------------

def find_more_than_avg(n,mark_list):
    total_mark=0
    for i in mark_list:
        total_mark+=i
    avg=total_mark/n
    count=0
    for i in mark_list:
        if i>avg:
            count+=1
    avg_percentage=count/n*100
    return avg_percentage

def generate_frequency(mark_list):
    freq=[]
    for x in range(26):
        count1=0
        for y in mark_list:
            if x==y:
                count1+=1
        freq.append(count1)
    return freq
def sort_marks(mark_list):
    mark_list=sorted(mark_list)
    return mark_list
n=10
mark_list=[12,18,25,24,2,5,18,20,20,21]
print(find_more_than_avg(n,mark_list))
print(generate_frequency(mark_list))
print(sort_marks(mark_list))

# ------------------------------------------------------------------------------------------

#word translator
dict1={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
eng=["merry","christmas"]
def trans(dict1,eng):
    eq = []
    for i in eng:
        eq.append(dict1[i])
    return eq

print(trans(dict1,eng))

# ------------------------------------------------------------------------------------------

#list comprehension

n1=int(input())
n2=int(input())
array=[i for i in range(n1,n2+1)]
print(array)
result=[]
for i in range(len(array)):#i=1
    for j in range(i,len(array)):#j=1,2
        result.append(array[i:j+1])#[0:1]=[1]
print(result)
result= [array[i:j+1] for i in range(len(array)) for j in range(i,len(array))]
print(result)
#[0:2]=[1,2]
c=0
for i in result:
    if sum(i)%2!=0:
        c+=1
print(c)




